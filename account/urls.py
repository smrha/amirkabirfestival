from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('edit/', views.profile_edit, name="edit"),
    path('education/', views.education_edit, name="education"),
    path('article/', views.ArticleCreateView.as_view(), name="article"),
    path('article/list', views.article_list, name="article_list"),
    path('article/edit/<int:id>', views.ArticleUpdateView.as_view(), name="article_edit"),
    path('ticket/add/', views.ticket_add, name='ticket_add'),
]
