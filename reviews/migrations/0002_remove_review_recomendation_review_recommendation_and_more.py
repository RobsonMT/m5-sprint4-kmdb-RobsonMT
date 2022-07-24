# Generated by Django 4.0.6 on 2022-07-24 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='recomendation',
        ),
        migrations.AddField(
            model_name='review',
            name='recommendation',
            field=models.CharField(blank=True, choices=[('Must Watch', 'Must'), ('Should Watch', 'Should'), ('Avoid Watch', 'Avoid'), ('No Opinion', 'No')], default='No Opinion', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
