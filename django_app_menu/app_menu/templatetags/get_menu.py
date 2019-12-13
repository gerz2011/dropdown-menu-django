from django import template
from django.db import connection
from app_menu.models import Menu

register = template.Library()



@register.inclusion_tag('include/menu.html', takes_context=True)
def draw_menu(context, slug):
    try:
        menu = Menu.objects.get(slug='main-menu')
        print(connection.queries)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}


"""
menu = Menu.objects.get(slug='main-menu')
[
{'sql': 'SELECT "app_menu_menu"."id", "app_menu_menu"."is_visible", "app_menu_menu"."order", "app_menu_menu"."date_created", "app_menu_menu"."date_updated", "app_menu_menu"."title", "app_menu_menu"."slug", "app_menu_menu"."named_url" FROM "app_menu_menu" WHERE "app_menu_menu"."slug" = \'main-menu\' LIMIT 21', 'time': '0.000'}
]

-----------------------------
menu = Menu.objects.prefetch_related('items').get(slug="main-menu")
[
{
'sql': 'SELECT "app_menu_menu"."id", "app_menu_menu"."is_visible", "app_menu_menu"."order", "app_menu_menu"."date_created", "app_menu_menu"."date_updated", "app_menu_menu"."title", "app_menu_menu"."slug", "app_menu_menu"."named_url" FROM "app_menu_menu" WHERE "app_menu_menu"."slug" = \'main-menu\' LIMIT 21', 
'time': '0.000'}, 
{
'sql': 'SELECT "app_menu_menuitem"."id", "app_menu_menuitem"."is_visible", "app_menu_menuitem"."order", "app_menu_menuitem"."date_created", "app_menu_menuitem"."date_updated", "app_menu_menuitem"."menu_id", "app_menu_menuitem"."parent_id", "app_menu_menuitem"."title", "app_menu_menuitem"."url", "app_menu_menuitem"."named_url" FROM "app_menu_menuitem" WHERE "app_menu_menuitem"."menu_id" IN (1) ORDER BY "app_menu_menuitem"."order" ASC',
'time': '0.000'}
]

"""