# Generated by Django 4.1.1 on 2022-12-06 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_description_alter_product_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
