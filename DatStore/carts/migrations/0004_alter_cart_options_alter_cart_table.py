# Generated by Django 4.1.1 on 2022-12-06 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cart_cart_id_alter_cart_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['id'], 'verbose_name': 'Carrito', 'verbose_name_plural': 'Carritos'},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Carrito',
        ),
    ]
