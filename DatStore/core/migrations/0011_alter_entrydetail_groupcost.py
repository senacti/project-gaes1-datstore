# Generated by Django 4.1.1 on 2022-12-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_inventoryentry_iduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrydetail',
            name='groupcost',
            field=models.PositiveIntegerField(default=0, verbose_name='Coste del grupo de productos'),
        ),
    ]
