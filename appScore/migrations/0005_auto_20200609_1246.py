# Generated by Django 3.0.7 on 2020-06-09 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appScore', '0004_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='average',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
