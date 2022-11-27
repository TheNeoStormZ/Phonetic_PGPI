# Generated by Django 4.1.1 on 2022-11-27 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0008_alter_cestaitem_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cesta',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='cesta',
            name='items',
        ),
        migrations.AddField(
            model_name='cesta',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.cestaitem'),
        ),
    ]
