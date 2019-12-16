from django import template
from django.db import connection
from app_menu.models import Menu, MenuItem
from django.db import reset_queries


register = template.Library()
  

@register.inclusion_tag('include/menu.html', takes_context=True)
def draw_menu(context, slug):
    try:
        # menu = Menu.objects.raw('SELECT * FROM app_menu_menuitem WHERE app_menu_menuitem.menu_id IN (1)')
        # menu = MenuItem.objects.raw('SELECT * FROM app_menu_menuitem')
        # menu = Menu.objects.prefetch_related('items').get(slug="main-menu")
        menu = MenuItem.objects.filter(menu__slug=slug)
        # menu = Menu.objects.get(slug=slug).filter()      

        # print(menu)


        print('======================================')
        print('SQL запрос draw_menu - ', connection.queries)
        print('запросов - ', len(connection.queries))
        reset_queries()
        print('--------------------------------------')

        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}


