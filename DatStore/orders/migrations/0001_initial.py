# Generated by Django 4.1.1 on 2022-12-07 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.common


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping_addresses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0005_alter_cartproducts_options_alter_cartproducts_cart_and_more'),
        ('promo_codes', '0002_alter_promocode_options_alter_promocode_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True, verbose_name='Codigo del Pedido')),
                ('status', models.CharField(choices=[(orders.common.OrderStatus['CREATED'], 'CREATED'), (orders.common.OrderStatus['PAYED'], 'PAYED'), (orders.common.OrderStatus['COMPLETED'], 'COMPLETED'), (orders.common.OrderStatus['CANCELED'], 'CANCELED')], default=orders.common.OrderStatus['CREATED'], max_length=50)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=1000, max_digits=8, verbose_name='Total del envio')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el:')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Carrito')),
                ('promo_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_codes.promocode', verbose_name='Codigo de promación')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_addresses.shippingaddress', verbose_name='Direccion del pedido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=150, verbose_name='Direccion a dónde irá el domicilio')),
                ('price', models.PositiveIntegerField(verbose_name='Precio del domicilio')),
                ('deliver', models.CharField(default='Repartidor', max_length=60, verbose_name='Nombre del repartidor')),
                ('idpedidoFK', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Identificación Pedido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Identificación del Usuario')),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilios',
                'db_table': 'Domicilios',
                'ordering': ['id'],
            },
        ),
    ]
