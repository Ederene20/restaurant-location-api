# Generated by Django 3.1.7 on 2021-04-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_auto_20210403_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(default=0),
        ),
    ]
