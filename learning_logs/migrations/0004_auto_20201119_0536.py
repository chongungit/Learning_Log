# Generated by Django 3.1.3 on 2020-11-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_entry_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
