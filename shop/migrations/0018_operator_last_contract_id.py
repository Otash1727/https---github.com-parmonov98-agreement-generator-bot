# Generated by Django 4.2.8 on 2024-03-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_customer_docx_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='last_contract_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]