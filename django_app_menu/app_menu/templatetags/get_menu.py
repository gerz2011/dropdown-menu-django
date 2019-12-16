from django import template
from app_menu.models import Menu, MenuItem

register = template.Library()

# сравниваем ссылку элемента меню с урл страницы, если совпадает- возвращаем строку activ
@register.simple_tag(takes_context=True)
def active_item_menu(context, path):
    if path in context.request.get_full_path():
        return 'active'
    else:
        return None

@register.inclusion_tag('include/menu.html', takes_context=True)
def draw_menu(context, slug):
    print('====================================================')
    try:
        items = MenuItem.objects.filter(menu__slug=slug)
        # items = MenuItem.objects.raw('SELECT * FROM app_menu_menuitem WHERE app_menu_menuitem.menu_slug = %s', [slug])
        return {'menu': items, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}
