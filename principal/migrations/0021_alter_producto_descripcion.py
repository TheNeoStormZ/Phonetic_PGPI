# Generated by Django 4.1.3 on 2022-12-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_pedido_saveinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=110),
        ),
    ]