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
    path('judgement/referee/<int:id>/', views.JudgementRefereeView.as_view(), name="judgement_referee"),
]
