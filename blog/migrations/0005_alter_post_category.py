# Generated by Django 5.1.2 on 2024-11-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DF', 'پیش فرض'), ('IM', 'اخبار مهم')], default='DF', max_length=2),
        ),
    ]
