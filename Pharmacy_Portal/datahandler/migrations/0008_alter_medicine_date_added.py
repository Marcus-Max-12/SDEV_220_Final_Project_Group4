# Generated by Django 5.2.3 on 2025-07-04 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0007_alter_medicine_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2025, 7, 4, 16, 2, 42, 275671), editable=False),
        ),
    ]
