# Generated by Django 5.2.3 on 2025-07-12 18:37

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_phone_number', models.CharField(max_length=10)),
                ('client_email', models.CharField(max_length=40)),
                ('client_address', models.CharField(max_length=50)),
                ('client_zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=128)),
                ('delivery_method', models.CharField(choices=[('CAP', 'Capsule'), ('LIQ', 'Liquid'), ('PIL', 'Pill'), ('INJ', 'Injection'), ('SKN', 'Transdermal'), ('INH', 'Inhalation')], default='Pill', max_length=3)),
                ('date_added', models.DateField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datahandler.client')),
                ('medication', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('quantity', models.PositiveBigIntegerField()),
                ('fulfillment', models.BooleanField(default=False)),
                ('date_prescribed', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='datahandler.client')),
            ],
            bases=('datahandler.client',),
        ),
    ]
