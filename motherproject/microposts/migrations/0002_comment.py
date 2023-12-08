# Generated by Django 4.2.7 on 2023-11-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='microposts.post', verbose_name='対象記事')),
            ],
            options={
                'verbose_name': 'コメント',
                'verbose_name_plural': 'コメント',
            },
        ),
    ]