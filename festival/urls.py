from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)