# Generated by Django 3.1.3 on 2020-12-02 21:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsApp', '0002_auto_20201201_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
