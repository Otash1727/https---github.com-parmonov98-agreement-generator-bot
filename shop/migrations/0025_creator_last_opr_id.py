# Generated by Django 4.2.8 on 2024-04-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_creator_msg_id2'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='last_opr_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
