from django.urls import path
from django.conf.urls.static import static
from portfolio import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog, name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)