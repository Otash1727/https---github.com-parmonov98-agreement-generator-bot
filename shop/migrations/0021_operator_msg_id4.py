# Generated by Django 4.2.8 on 2024-04-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_operator_msg_id3'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='msg_id4',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
