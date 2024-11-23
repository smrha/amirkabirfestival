from django.contrib import admin

from .models import Profile, Education, Article, Ticket


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'author_name', 'title', 'teacher']
    raw_id_fields = ['user']

    def author_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'father_name', 'national_id']
    raw_id_fields = ['user']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user']
    raw_id_fields = ['user']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator']
