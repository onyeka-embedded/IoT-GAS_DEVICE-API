# Generated by Django 4.2.7 on 2023-11-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_api', '0002_gas_hum_gas_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gas',
            name='co2',
        ),
        migrations.AddField(
            model_name='gas',
            name='co',
            field=models.CharField(default=0, max_length=10, verbose_name='CO'),
            preserve_default=False,
        ),
    ]