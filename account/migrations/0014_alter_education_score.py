# Generated by Django 5.1.2 on 2024-12-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
