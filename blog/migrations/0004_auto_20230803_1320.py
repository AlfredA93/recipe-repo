# Generated by Django 3.2.20 on 2023-08-03 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230803_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]