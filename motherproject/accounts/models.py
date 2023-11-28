from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.urls import reverse_lazy

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, age=None):
        if not email:
            raise ValueError('Enter Email') 
        user = self.model(
            username=username,
            email=email,
            age=age
        )
        user.set_password(password) 
        user.save(using=self._db) 
        return user

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    age = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)  

    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    twitter_id = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.CharField(max_length=255, blank=True, null=True)

    last_login_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 


    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')
    
    favourite_post = models.ManyToManyField(
        'microposts.Post', blank=True, verbose_name='お気に入り投稿'
    )

    
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')

class Relationship(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='user-relationship')
        ]

    def __str__(self):
        return"{}:{}".format(self.follower.username, self.following.username)    