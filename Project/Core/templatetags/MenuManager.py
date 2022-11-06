from django import template


class MenuElem:
    def __init__(self, title, url_name):
        self.title = title
        self.url_name = url_name
        self.is_active = False


class Menus:
    ''' Класс для хранения кастомных меню '''

    main_menu = [
        MenuElem('Главная', 'homepage:home'),
        MenuElem('Описание', 'about:about'),
        MenuElem('Каталог', 'catalog:item_list'),
    ]


register = template.Library()


@register.inclusion_tag('header.html')
def get_main_menu(request):
    menu = []
    for elem in Menus.main_menu:
        elem.is_active = elem.url_name == request.resolver_match.view_name
        menu.append(elem)

    return {"menu": menu}
