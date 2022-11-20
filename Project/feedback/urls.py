from django.urls import path

from . import views
from .apps import FeedbackConfig

app_name = FeedbackConfig.name

urlpatterns = [
    path('', views.CreateFeedback.as_view(), name='feedback'),
]
