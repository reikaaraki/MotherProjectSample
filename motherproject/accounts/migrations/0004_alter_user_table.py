# Generated by Django 4.2.7 on 2023-11-27 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]
