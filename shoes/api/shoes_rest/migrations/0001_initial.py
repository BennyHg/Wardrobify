# Generated by Django 4.0.3 on 2022-07-28 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=100)),
                ('bin_number', models.PositiveSmallIntegerField()),
                ('bin_size', models.PositiveSmallIntegerField()),
                ('bin_id', models.PositiveSmallIntegerField(null=True)),
                ('href', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('picture', models.URLField(null=True)),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shoes', to='shoes_rest.binvo')),
            ],
        ),
    ]
