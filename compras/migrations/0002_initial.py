# Generated by Django 5.1.3 on 2024-12-03 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compras', '0001_initial'),
        ('juegos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='juego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.juego'),
        ),
    ]
