# Generated by Django 5.1.2 on 2024-10-25 22:27

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='defense_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True),
        ),
    ]
