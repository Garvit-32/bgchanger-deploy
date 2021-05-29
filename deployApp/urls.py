from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'deployApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('predictImage', views.predictImage, name='predictImage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
