# Generated by Django 4.2.1 on 2023-05-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customers_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
