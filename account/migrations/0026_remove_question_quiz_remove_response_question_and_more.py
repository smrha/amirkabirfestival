# Generated by Django 5.1.2 on 2024-12-28 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_response_assistant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.RemoveField(
            model_name='response',
            name='article',
        ),
        migrations.RemoveField(
            model_name='response',
            name='assistant',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
