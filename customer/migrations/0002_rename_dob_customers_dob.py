# Generated by Django 4.2.1 on 2023-05-13 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='DOB',
            new_name='dob',
        ),
    ]
