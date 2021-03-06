# Generated by Django 3.1.7 on 2021-03-19 11:51

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_restaurant_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=django.contrib.gis.geos.point.Point(12.3, 14.88), null=True, srid=4326),
        ),
    ]
