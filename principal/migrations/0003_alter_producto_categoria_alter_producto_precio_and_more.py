# Generated by Django 4.1.1 on 2022-11-20 11:56

import django.core.validators
from django.db import migrations, models
import principal.models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_producto_categoria_producto_secciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Funda', 'Funda'), ('Cargadores', 'Cargadores'), ('Protectores', 'Protectores'), ('Otros', 'Otros')], default=principal.models.ProductType['OTRO'], max_length=15),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='secciones',
            field=models.CharField(choices=[('Huawei', 'Huawei'), ('Xiaomi', 'Xiaomi'), ('Samsung', 'Samsung'), ('Vivo', 'Vivo'), ('Desconocido', 'Desconocido')], default=principal.models.ProductSections['UNK'], max_length=15),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
