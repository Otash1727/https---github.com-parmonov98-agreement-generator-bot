# Generated by Django 4.2.8 on 2024-03-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_debtors_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='operator_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
