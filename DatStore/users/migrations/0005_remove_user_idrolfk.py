# Generated by Django 4.1.1 on 2022-12-13 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_idrolfk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='idrolfk',
        ),
    ]