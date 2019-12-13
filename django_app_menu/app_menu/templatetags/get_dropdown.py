from django import template

register = template.Library()

# сравниваем ссылку элемента меню с урл страницы, если совпадает- возвращаем строку activ
@register.simple_tag(takes_context=True)
def active_item_menu(context, path):
    if path in context.request.get_full_path():
        return 'active'
    else:
        return None


@register.inclusion_tag('include/item-dropdown.html', takes_context=True)
def draw_dropdown(context, item):
    full_path = context.request.get_full_path()
    return {'item': item, 'full_path': full_path}


@register.inclusion_tag('include/item-dropdown.html', takes_context=True)
def draw_dropdown_in(context, item):
    return {'item': item }

