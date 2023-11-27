# Generated by Django 4.2.7 on 2023-11-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microposts', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourite_post',
            field=models.ManyToManyField(blank=True, to='microposts.post', verbose_name='お気に入り投稿'),
        ),
    ]
