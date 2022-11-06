from django.urls import path, re_path

from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    re_path(
        r'^(?P<item_id>[1-9]\d*)/$', views.ItemDetail.as_view(),
        name='item_detail'
        )
]
