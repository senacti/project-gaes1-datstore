# Generated by Django 4.1.1 on 2022-12-12 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_entrydetail_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='idrolfk',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]