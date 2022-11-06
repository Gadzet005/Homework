from django.views.generic import ListView, DetailView

from .models import Item


class ItemList(ListView):
    template_name = "catalog/item_list.html"
    model = Item
    context_object_name = 'item_list'
    extra_context = {
        'title_name': 'Каталог'
    }


class ItemDetail(DetailView):
    template_name = "catalog/item_detail.html"
    model = Item
    pk_url_kwarg = "item_id"
    context_object_name = "item"
    extra_context = {
        'title_name': 'Детали предмета'
    }
