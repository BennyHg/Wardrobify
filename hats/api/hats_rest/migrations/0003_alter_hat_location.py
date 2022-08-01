# Generated by Django 4.0.3 on 2022-07-28 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0002_locationvo_import_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hat',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hats', to='hats_rest.locationvo'),
        ),
    ]