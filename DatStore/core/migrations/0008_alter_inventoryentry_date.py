# Generated by Django 4.1.1 on 2022-12-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryentry',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha entrada'),
        ),
    ]
