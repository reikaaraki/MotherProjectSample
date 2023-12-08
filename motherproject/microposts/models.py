from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils import timezone

class Post(models.Model):
    
    owner = models.ForeignKey('accounts.User', verbose_name='オーナー', on_delete=models.CASCADE)
    title = models.CharField(max_length=15, default='')
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'posts'


class Comment(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事', related_name='comments')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'