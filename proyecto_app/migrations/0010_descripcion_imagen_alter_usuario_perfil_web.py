# Generated by Django 4.0.4 on 2022-07-05 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0009_alter_usuario_perfil_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcion',
            name='imagen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_perfil', to='proyecto_app.usuario_perfil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario_perfil',
            name='web',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
