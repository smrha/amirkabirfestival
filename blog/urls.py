from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('gallery/1/', views.gallery_first, name='gallery_first'),
    path('gallery/2/', views.gallery_second, name='gallery_second'),
    path('gallery/3/', views.gallery_third, name='gallery_third'),
    path('farakhan/', views.farakhan, name='farakhan'),
    path('about/', views.about, name='about'),
    path('olom_payeh/', views.olom_payeh, name='olom_payeh'),
    path('olom_ensani/', views.olom_ensani, name='olom_ensani'),
    path('fani/', views.fani, name='fani'),
    path('keshavarzi/', views.keshavarzi, name='keshavarzi'),
    path('pezeshki/', views.pezeshki, name='pezeshki'),
    path('dampezeshki/', views.dampezeshki, name='dampezeshki'),
    path('honar/', views.honar, name='honar'),
    path('introduction/', views.introduction, name='introduction'),
    path('foundation/', views.foundation, name='foundation'),
    path('purpose/', views.PurposeView.as_view(), name='purpose'),
    path('executive/', views.executive, name='executive'),
    path('news/', views.news, name='news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    # path('<int:post_id>/share/',
    #      views.post_share, name='post_share'),
    # path('<int:post_id>/comment/',
    #      views.post_comment, name='post_comment'),
]