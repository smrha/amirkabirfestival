# Generated by Django 5.1.2 on 2024-12-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_judgement_assistant_alter_judgement_referee'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education_group',
            field=models.CharField(choices=[('هنر و معماری', 'Art'), ('علوم انسانی', 'Humanities'), ('فنی و مهندسی', 'Engineering'), ('علوم پایه', 'Science'), ('کشاورزی، منابع طبیعی و محیط زیست', 'Agricultural'), ('علوم پزشکی', 'Medical'), ('دامپزشکی و علوم دامی', 'Veterinary')], default='فنی و مهندسی', max_length=32),
        ),
    ]
