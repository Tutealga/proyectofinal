# Generated by Django 4.0.4 on 2022-07-02 00:21

import django.contrib.auth.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_perfil',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name=django.contrib.auth.forms.UserCreationForm),
            preserve_default=False,
        ),
    ]