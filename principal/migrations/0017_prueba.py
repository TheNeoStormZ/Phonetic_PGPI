# Generated by Django 4.1.1 on 2022-11-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_remove_pedido_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
