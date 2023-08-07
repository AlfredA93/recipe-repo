# Generated by Django 3.2.20 on 2023-08-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230803_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='placeholder', max_length=140, unique=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='summary',
            field=models.TextField(default='placeholder', max_length=240),
        ),
    ]