# Generated by Django 4.1.1 on 2022-12-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_inventoryentry_totalpurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrydetail',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Cantidad de la entrada'),
        ),
    ]
