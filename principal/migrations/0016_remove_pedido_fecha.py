# Generated by Django 4.1.1 on 2022-11-27 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_pedido_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
    ]