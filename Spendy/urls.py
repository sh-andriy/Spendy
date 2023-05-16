from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('transactions/', include('transactions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
