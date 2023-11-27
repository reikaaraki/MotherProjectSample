from django.db import models
from accounts.models import User

class Post(models.Model):
    
    owner = models.ForeignKey('accounts.User', verbose_name='オーナー', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'posts'


