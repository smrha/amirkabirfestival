# Generated by Django 5.1.2 on 2024-11-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DF', 'پیش فرض'), ('IM', 'اخبار مهم')], default='IM', max_length=2),
        ),
    ]