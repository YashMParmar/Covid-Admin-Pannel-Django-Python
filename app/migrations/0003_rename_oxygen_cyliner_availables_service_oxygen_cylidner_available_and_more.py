# Generated by Django 4.1.7 on 2023-03-14 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_service_delete_sevice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='oxygen_cyliner_availables',
            new_name='oxygen_cylidner_available',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='oxygen_cyliner_total',
            new_name='oxygen_cylinder_total',
        ),
    ]
