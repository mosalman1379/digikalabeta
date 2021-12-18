# Generated by Django 4.0 on 2021-12-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phoneInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneUrl', models.URLField(verbose_name='phone link')),
                ('phoneName', models.CharField(max_length=40, verbose_name='phone name')),
                ('phonePrice', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('phoneBeforeDiscount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('phonePicLink', models.URLField(verbose_name='phone picture link')),
                ('rateQuality', models.FloatField(default=0.0, max_length=5.0)),
                ('rateBuy', models.FloatField(default=0.0, max_length=5.0)),
                ('rateCreativeness', models.FloatField(default=0.0, max_length=5.0)),
                ('rateFeature', models.FloatField(default=0.0, max_length=5.0)),
                ('rateSimplicity', models.FloatField(default=0.0, max_length=5.0)),
                ('rateDesign', models.FloatField(default=0.0, max_length=5.0)),
            ],
        ),
    ]
