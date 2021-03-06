# Generated by Django 4.0.4 on 2022-07-04 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0004_usuario_perfil_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModificacionesFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('direccion', models.ImageField(upload_to='banner_image')),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('creditos', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'modificacion footer',
                'verbose_name_plural': 'modificaciones footer',
            },
        ),
        migrations.AlterField(
            model_name='usuario_perfil',
            name='web',
            field=models.URLField(max_length=300),
        ),
    ]
