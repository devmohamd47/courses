# Generated by Django 4.2.2 on 2023-06-25 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('available_courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='pirce',
            new_name='price',
        ),
    ]