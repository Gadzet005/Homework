from django.urls import path

from . import views
from .apps import AboutConfig

app_name = AboutConfig.name

urlpatterns = [
    path('', views.About.as_view(), name='about'),
]
