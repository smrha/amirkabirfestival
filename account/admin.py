from django.contrib import admin

from .models import Profile, Education, Article, Ticket, Judgement, Quiz

@admin.register(Judgement)
class JudgementAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'author_name', 'get_mobile', 'get_email', 'title', 'teacher']
    raw_id_fields = ['user']

    def author_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_mobile(self, obj):
        return obj.user.profile.mobile_number
    
    def get_email(self, obj):
        return obj.user.email


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'father_name', 'national_id']
    raw_id_fields = ['user']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'user__first_name', 'user__last_name', 'university', 'field_study', 'degree']
    raw_id_fields = ['user']


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['article__title', 'assistant__first_name', 'assistant__last_name', 'result']


# @admin.register(Response)
# class ResponseAdmin(admin.ModelAdmin):
#     pass
