from django.urls import path

from . import views
from .apps import HomepageConfig

app_name = HomepageConfig.name

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
