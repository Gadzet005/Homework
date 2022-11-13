from django.views.generic import ListView, DetailView

from .models import Item


class ItemList(ListView):
    template_name = "catalog/item_list.html"
    queryset = Item.objects.published().order_by('category__name', 'name')
    context_object_name = 'items'
    extra_context = {
        'title_name': 'Каталог'
    }


class ItemDetail(DetailView):
    template_name = "catalog/item_detail.html"
    queryset = Item.objects.published()
    pk_url_kwarg = "item_id"
    context_object_name = "item"
    extra_context = {
        'title_name': 'Детали товара'
    }
