from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('edit/', views.profile_edit, name="edit"),
    path('education/', views.education_edit, name="education"),
    path('article/', views.ArticleCreateView.as_view(), name="article"),
    path('article/list/', views.ArticleListView.as_view(), name="article_list"),
    path('article/<int:id>/', views.ArticleShowView.as_view(), name="article_show"),
    path('articles/', views.UserArticleListView.as_view(), name="user_articles"),
    path('article/edit/<int:id>', views.ArticleUpdateView.as_view(), name="article_edit"),
    path('ticket/add/', views.ticket_add, name='ticket_add'),

    path('judgement/list/', views.JudgementListView.as_view(), name="judgement_list"),
    path('judgement/status', views.ArticleListJudgementStatus.as_view(), name="judgement_status"),
    path('judgement/referee/<int:id>/', views.JudgementRefereeView.as_view(), name="judgement_referee"),
    path('assistant/list/', views.JudgementAssistantListView.as_view(), name="assistant_list"),
    path('judgement/assistant/<int:id>/', views.JudgementAssistantView.as_view(), name="judgement_assistant"),
    path('judge/list/', views.JudgementJudgeListView.as_view(), name="judge_list"),
    path('judge/<int:id>/', views.JudgementJudgeView.as_view(), name="judge"),
    path('export_to_excel/', views.export_to_excel, name='export'),

    path('arbitration/<int:id>/', views.ArbitrationShowView.as_view(), name='arbitration')
]
