# Generated by Django 4.1 on 2022-10-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id del Usuario'),
        ),
    ]
