# Generated by Django 3.2.5 on 2022-01-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questao7', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
