from django import template
from django.template import Variable, VariableDoesNotExist

register = template.Library()


# Trata a pesquisa + paginação
#
@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


# Renderiza a TD de acordo com o tipo do campo
#
@register.simple_tag()
def render_td(value, type):
    if value is None:
        value = '<span class="label label-inline label-light-secondary font-weight-bold text-dark-50"> ? </span>'

    if type == 'CharField':
        return '<td>{}</td>'.format(value)
    elif type == 'IntegerField':
        return '<td>{}</td>'.format(value)
    elif type == 'BooleanField':
        if value:
            return '<td><span class="label label-inline label-light-success font-weight-bold"> Sim </span></td>'
        else:
            return '<td><span class="label label-inline label-light-danger font-weight-bold"> Não </span></td>'


# Recupera o valor do Object de acordo com uma string
#
@register.filter
def hash(object, attr):
    pseudo_context = {'object': object}
    try:
        value = Variable('object.%s' % attr).resolve(pseudo_context)
    except VariableDoesNotExist:
        value = None
    return value
