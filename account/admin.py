from django.contrib import admin

from .models import Profile, Education, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'teacher']
    raw_id_fields = ['user']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'father_name', 'national_id']
    raw_id_fields = ['user']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user']
    raw_id_fields = ['user']
