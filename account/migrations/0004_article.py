# Generated by Django 5.1.2 on 2024-10-20 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_education_univesity_education_university_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('education_group', models.CharField(max_length=64)),
                ('teacher', models.CharField(max_length=120)),
                ('teacher_mobile', models.CharField(max_length=11)),
                ('teacher_email', models.CharField(max_length=120)),
                ('adviser', models.CharField(max_length=120)),
                ('adviser_mobile', models.CharField(max_length=11)),
                ('adviser_email', models.CharField(max_length=120)),
                ('article_score', models.IntegerField()),
                ('type', models.CharField(max_length=32)),
                ('Requester', models.CharField(max_length=120)),
                ('Requester_loc', models.CharField(max_length=120)),
                ('summary', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
