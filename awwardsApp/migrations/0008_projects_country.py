# Generated by Django 3.1.3 on 2020-12-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsApp', '0007_auto_20201203_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='country',
            field=models.CharField(default='e.g. timezone.now', max_length=50),
            preserve_default=False,
        ),
    ]