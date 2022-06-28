# Generated by Django 4.0.4 on 2022-06-27 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcion',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='proyecto_app.usuarios'),
            preserve_default=False,
        ),
    ]
