# Generated by Django 4.0.3 on 2022-07-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationvo',
            name='import_href',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
