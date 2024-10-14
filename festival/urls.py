from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('article.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
