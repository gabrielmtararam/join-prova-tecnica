# Generated by Django 3.2.5 on 2022-01-05 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questao1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoas',
            name='legal',
        ),
        migrations.AddField(
            model_name='pessoas',
            name='cargo',
            field=models.ForeignKey(db_column='id_cargo', null=True, on_delete=django.db.models.deletion.CASCADE, to='questao1.cargos'),
        ),
        migrations.AlterField(
            model_name='cargos',
            name='nome_cargo',
            field=models.CharField(db_column='nome_cargo', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='admissao',
            field=models.DateField(db_column='admissao', default=datetime.datetime.now, verbose_name='Admissao'),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='nome',
            field=models.CharField(db_column='nome', max_length=200, verbose_name='Nome '),
        ),
    ]
