# Generated by Django 4.2.4 on 2023-10-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ordenes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('DPI', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('edad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tarjeta', models.CharField(max_length=20, unique=True)),
                ('CVV', models.CharField(max_length=3)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_final', models.DateField()),
                ('idBanco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.banco')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('idProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedor')),
            ],
        ),
    ]
