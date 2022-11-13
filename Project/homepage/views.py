from django.views.generic import ListView

from catalog.models import Item


class Home(ListView):
    template_name = "homepage/index.html"
    queryset = Item.objects.on_main()
    context_object_name = 'items'
    extra_context = {
        'title_name': 'Главная страница'
    }
