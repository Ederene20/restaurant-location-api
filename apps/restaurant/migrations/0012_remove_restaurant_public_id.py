# Generated by Django 3.1.7 on 2021-03-21 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_auto_20210319_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='public_id',
        ),
    ]