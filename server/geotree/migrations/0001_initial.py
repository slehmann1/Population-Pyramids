# Generated by Django 4.1.5 on 2023-01-24 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geogcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GeoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('age', models.IntegerField()),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('geo_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='geotree.geoname')),
            ],
        ),
    ]
