# Generated by Django 3.1.7 on 2021-03-19 12:33

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20210319_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326),
        ),
    ]
