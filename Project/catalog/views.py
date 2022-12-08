from django.views.generic import DetailView, ListView

from catalog.models import Item
from rating.models import ItemRating


class ItemList(ListView):
    template_name = 'catalog/item_list.html'
    queryset = Item.objects.published().order_by('category__name', 'name')
    context_object_name = 'items'
    extra_context = {
        'title_name': 'Каталог'
    }


class ItemDetail(DetailView):
    template_name = 'catalog/item_detail.html'
    queryset = Item.objects.published()
    pk_url_kwarg = 'item_id'
    context_object_name = 'item'
    extra_context = {
        'title_name': 'Детали товара'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_rating = ItemRating.objects.get_rating_of_item(self.object)
        user_rating = ItemRating.objects.get_rating_of_user(
            self.object, self.request.user
            )
        return {**context, **item_rating, 'user_rating': user_rating}
