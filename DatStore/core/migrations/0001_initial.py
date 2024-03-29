# Generated by Django 4.1 on 2022-10-25 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre del Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'db_table': 'Rol',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del proveedor')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre del proveedor')),
                ('phone', models.IntegerField(verbose_name='Número de telefono')),
                ('email', models.CharField(max_length=30, verbose_name='Email del proveedor')),
                ('direction', models.CharField(max_length=50, verbose_name='Direccion del proveedor')),
                ('state', models.CharField(max_length=15, verbose_name='Estado del proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Preveedores',
                'db_table': 'Proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre del Producto')),
            ],
            options={
                'verbose_name': 'Tipo de Producto',
                'verbose_name_plural': 'Tipo de Productos',
                'db_table': 'TipoProducto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WayToPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Nombre de la forma de pago')),
            ],
            options={
                'verbose_name': 'Forma de Pago',
                'verbose_name_plural': 'Formas de Pago',
                'db_table': 'FormaPago',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id del Usuario')),
                ('name', models.CharField(max_length=20, verbose_name='Primer nombre del Usuario')),
                ('names', models.CharField(max_length=20, verbose_name='Segundo nombre del Usuario')),
                ('lastn', models.CharField(max_length=20, verbose_name='Primer apellido del Usuario')),
                ('lastns', models.CharField(max_length=20, verbose_name='Segundo apellido del Usuario')),
                ('address', models.CharField(max_length=50, verbose_name='Direccion del Usuario')),
                ('email', models.CharField(max_length=30, verbose_name='Correo del Usuario')),
                ('password', models.CharField(max_length=20, verbose_name='Contraseña del Usuario')),
                ('telephone', models.BigIntegerField(verbose_name='Numero del Celular')),
                ('condition', models.CharField(max_length=15, verbose_name='Estado del Usuario')),
                ('idrolfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol', verbose_name='Identificación del Rol')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre del producto')),
                ('costp', models.BigIntegerField(blank=True, default=10, null=True, verbose_name='Precio producto indiv.')),
                ('stock', models.IntegerField(verbose_name='Cantidad del producto')),
                ('state', models.CharField(choices=[('Act', 'Active'), ('Ina', 'Inactive')], default='Activo', max_length=20, verbose_name='Estado del producto')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='productos/')),
                ('idfksup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.supplier', verbose_name='Idenfiticación del Proveedor')),
                ('idfktipp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typeproduct', verbose_name='Identificación del Tipo Producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre del permiso')),
                ('idprodFK', models.ManyToManyField(to='core.rol', verbose_name='Nombre del Rol')),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Permiso',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha del pedido')),
                ('total', models.BigIntegerField(verbose_name='Total del pedido')),
                ('typedel', models.CharField(choices=[('Dom', 'Domicilio'), ('Tie', 'Tienda')], max_length=4, verbose_name='Tipo Entrega')),
                ('statord', models.CharField(choices=[('Ent', 'Entregado'), ('Pen', 'Pendiente')], max_length=4, verbose_name='Estado Entrega')),
                ('refpay', models.CharField(max_length=20, null=True, verbose_name='Referencia de pago')),
                ('idfkclient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', verbose_name='Identificación Cliente')),
                ('idfkpayform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.waytopay', verbose_name='Identificación Forma Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Inventoryoutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Cantidad de la Salida')),
                ('dateout', models.DateField(verbose_name='Fecha de la Salida')),
                ('iddepefk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order', verbose_name='Identificación Detalle Pedido')),
                ('idprofk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Identificación Producto')),
            ],
            options={
                'verbose_name': 'Salida del inventario',
                'verbose_name_plural': 'Salidas del inventario',
                'db_table': 'SalidaInventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InventoryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha entrada')),
                ('totalpurchase', models.IntegerField(verbose_name='Total Compra')),
                ('refpayment', models.CharField(max_length=10, verbose_name='Referencia de pago')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', verbose_name='Identificación del Usuario')),
                ('idwaytopay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.waytopay', verbose_name='Identificación Forma Pago')),
            ],
            options={
                'verbose_name': 'EntradaInventario',
                'verbose_name_plural': 'EntradasInventario',
                'db_table': 'EntradaInventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Cantidad de la entradad')),
                ('dateexpiry', models.DateField(verbose_name='Fecha caducidad de los productos')),
                ('purchaseprice', models.BigIntegerField(verbose_name='Precio de compra de los productos')),
                ('groupcost', models.BigIntegerField(verbose_name='Coste del grupo de productos')),
                ('identinvFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventoryentry', verbose_name='Identificación Entrada Inventario')),
                ('idprodFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Identificación del producto')),
            ],
            options={
                'verbose_name': 'DetalleEntrada',
                'verbose_name_plural': 'DetallesEntrada',
                'db_table': 'DetalleEntrada',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField(verbose_name='Cantidad productos')),
                ('costgp', models.BigIntegerField(verbose_name='Precio grupo producto')),
                ('idfkord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order', verbose_name='Identificación Pedidos')),
                ('idfkprod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Ifentificación Producto')),
            ],
            options={
                'verbose_name': 'Detalle Pedido',
                'verbose_name_plural': 'Detalles Pedido',
                'db_table': 'Detallepedido',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=60, verbose_name='Direccion a dónde irá el domicilio')),
                ('price', models.BigIntegerField(verbose_name='Precio del domicilio')),
                ('idEmpleadoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', verbose_name='Identificación Empleado')),
                ('idPedidoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order', verbose_name='Identificación Pedido')),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilios',
                'db_table': 'Domicilios',
                'ordering': ['id'],
            },
        ),
    ]
