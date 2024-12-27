# Generated by Django 5.1.2 on 2024-12-26 17:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_judgement_article_alter_judgement_referee'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgement',
            name='referee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judgements', to=settings.AUTH_USER_MODEL, verbose_name='داور'),
        ),
    ]
