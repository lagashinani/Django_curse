from django import template


register = template.Library()


@register.filter
def background_color_cell(value):
    try:
        value = float(value)
        if value < 0:
            return 'green'
        elif value < 1:
            return 'white'
        elif value < 2:
            return 'lightcoral '
        elif value < 5:
            return 'crimson'
        return 'red'
    except ValueError:
        return 'white'
