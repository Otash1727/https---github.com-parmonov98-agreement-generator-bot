# Generated by Django 4.2.8 on 2024-03-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_customer_passport_infos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_issue',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='passport_infos',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
