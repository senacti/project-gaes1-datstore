# Generated by Django 4.1.1 on 2022-12-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_inventoryentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryentry',
            name='totalpurchase',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Total Compra'),
        ),
    ]
