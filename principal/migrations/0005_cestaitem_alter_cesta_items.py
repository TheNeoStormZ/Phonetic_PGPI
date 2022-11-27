# Generated by Django 4.1.3 on 2022-11-26 13:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_cesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='CestaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='principal.producto')),
            ],
        ),
        migrations.AlterField(
            model_name='cesta',
            name='items',
            field=models.ManyToManyField(to='principal.cestaitem'),
        ),
    ]
