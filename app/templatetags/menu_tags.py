from django import template
from app.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = MenuItem.objects.filter(title=menu_name).get()
    except MenuItem.DoesNotExist:
        return ''

    request = context['request']
    current_url = request.path

    def render_menu_item(item):
        active_class = 'active' if current_url == item.url else ''
        children = item.children.all()

        if children:
            submenu = '<ul>'
            for child in children:
                submenu += f'<li>{render_menu_item(child)}</li>'
            submenu += '</ul>'
        else:
            submenu = ''

        if item.url:
            return f'<a href="{item.url}" class="{active_class}">{item.title}</a>{submenu}'
        else:
            return f'<span class="{active_class}">{item.title}</span>{submenu}'

    return mark_safe(render_menu_item(menu))
