# Generated by Django 4.1.7 on 2023-03-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_availability_available_availability_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
