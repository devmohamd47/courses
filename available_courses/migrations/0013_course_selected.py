# Generated by Django 4.2.2 on 2023-07-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('available_courses', '0012_alter_teachrequest_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
