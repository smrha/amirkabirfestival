# Generated by Django 5.1.2 on 2024-12-26 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_quiz_profile_type_question_response'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgement',
            name='referee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judgements', to=settings.AUTH_USER_MODEL, verbose_name='داور'),
        ),
    ]
