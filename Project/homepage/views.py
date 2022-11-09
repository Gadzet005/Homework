from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "homepage/index.html"
    extra_context = {
        'title_name': 'Главная страница'
    }
