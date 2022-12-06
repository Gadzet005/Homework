from django.urls import path

from rating.views import CreateItemRating

app_name = 'rating'

urlpatterns = [
    path('<item_id>/', CreateItemRating.as_view(), name='set_rating'),
]
