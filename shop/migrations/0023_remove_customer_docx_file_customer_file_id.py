# Generated by Django 4.2.8 on 2024-04-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_alter_customer_docx_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='docx_file',
        ),
        migrations.AddField(
            model_name='customer',
            name='File_ID',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]