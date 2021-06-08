from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from apps.core.defs import is_valid_user
from bluedata.helpers import reverse_url


# Seta o contexto do List
#
def set_context_list(context, self):
    # Variables
    url = self.base_url
    title = self.template_title

    # Set menu on session
    self.request.session['menu'] = self.access['menu']
    self.request.session['item'] = self.access['item']

    # Templates
    context['template'] = 'keen.html'
    context['template_title'] = title
    context['template_subtitle'] = 'listar'
    context['template_url_clear'] = reverse_url('{}_list'.format(url))
    context['template_url_update'] = '{}_update'.format(url)
    context['template_table_head'] = 'bluedata_interface/template_table_head.html'
    context['template_table_row'] = 'bluedata_interface/template_table_row.html'

    btn_add = set_button('Adicionar', reverse_url('{}_create'.format(url)), 'btn-primary', 'la la-plus')
    context['template_buttons'] = [btn_add]


# Seta o contexto do Create
#
def set_context_create(context, self):
    # Variables
    url = self.base_url
    title = self.template_title

    # Set session and menu
    self.request.session['menu'] = self.access['menu']
    self.request.session['item'] = self.access['item']
    self.request.session['uuid'] = None

    # Templates
    context['template'] = 'keen.html'
    context['template_title'] = title
    context['template_subtitle'] = 'adicionar'
    context['template_form_fields'] = 'bluedata_interface/template_form_render.html'
    context['template_btn_save'] = True

    btn_back = set_button('Voltar', reverse_url('{}_list'.format(url)), 'btn-outline-secondary', 'la la-angle-left')
    context['template_buttons'] = [btn_back]


# Seta o contexto do Update
#
def set_context_update(context, self):
    # Variables
    url = self.base_url
    title = self.template_title

    # Set session and menu
    self.request.session['menu'] = self.access['menu']
    self.request.session['item'] = self.access['item']
    self.request.session['uuid'] = str(self.object.id)

    # Templates
    context['template'] = 'keen.html'
    context['template_title'] = title
    context['template_subtitle'] = 'alterar'
    context['template_url_delete'] = reverse_url('{}_delete'.format(url), [str(self.object.id)])
    context['template_url_active'] = reverse_url('{}_active'.format(url), [str(self.object.id)])
    context['template_form_fields'] = 'bluedata_interface/template_form_render.html'
    context['template_btn_save'] = True

    btn_back = set_button('Voltar', reverse_url('{}_list'.format(url)), 'btn-outline-secondary', 'la la-angle-left')
    context['template_buttons'] = [btn_back]


# Seta o contexto do Delete
#
def set_context_delete(context, self):
    # Variables
    url = self.base_url
    title = self.template_title

    # Set session and menu
    self.request.session['menu'] = self.access['menu']
    self.request.session['item'] = self.access['item']

    # Templates
    context['template'] = 'keen.html'
    context['template_title'] = title
    context['template_subtitle'] = 'excluir'

    btn_back = set_button('Voltar', reverse_url('{}_update'.format(url), [str(self.object.id)]), 'btn-outline-secondary', 'la la-angle-left')
    context['template_buttons'] = [btn_back]


# Metodo get da BaseActiveView
#
def get_base_active_view(self, kwargs):
    # Set session and menu
    self.request.session['menu'] = self.access['menu']
    self.request.session['item'] = self.access['item']

    # Check permission
    if not is_valid_user(self.request.user, self.access):
        logout(self.request)
        return HttpResponseRedirect(reverse_url('account_login'))

    msg = toggle_active(self.model.objects.get(id=kwargs['pk']))
    set_message(self, msg)
    return HttpResponseRedirect(reverse_url('{}_list'.format(self.base_url)))


# Dado um modelo modifica o status is_active
#
def toggle_active(modelo):
    if modelo.is_active:
        modelo.is_active = False
        msg = 'Registro alterado para inativo'
    else:
        modelo.is_active = True
        msg = 'Registro alterado para ativo'
    modelo.save()
    return msg


# Seta a mensagem para o template
#
def set_message(self, msg):
    messages.add_message(self.request, messages.SUCCESS, msg)


# Seta um botão para o template
#
def set_button(title, url, color, icon):
    return {'title': title, 'url': url, 'color': color, 'icon': icon}
