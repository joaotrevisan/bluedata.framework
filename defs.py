from django.contrib import messages

from bluedata.helpers import reverse_url


# Seta o contexto do List
#
def set_context_list(context, url, title):
    context['template_title'] = title
    context['template_subtitle'] = 'listar'
    context['template_url_clear'] = reverse_url('{}_list'.format(url))
    context['template_url_update'] = '{}_update'.format(url)
    context['template_table_head'] = 'bluedata/template_table_head.html'
    context['template_table_row'] = 'bluedata/template_table_row.html'
    context['template_buttons'] = [set_button('Adicionar', reverse_url('{}_create'.format(url)), 'btn-primary',
                                              'la la-plus')]


# Seta o contexto do Create
#
def set_context_create(context, self, url, title):
    self.request.session['uuid'] = None
    context['template_title'] = title
    context['template_subtitle'] = 'adicionar'
    context['template_form_fields'] = 'bluedata/template_form_render.html'
    context['template_btn_save'] = True
    context['template_buttons'] = [set_button('Voltar', reverse_url('{}_list'.format(url)), 'btn-outline-secondary',
                                              'la la-angle-left')]


# Seta o contexto do Update
#
def set_context_update(context, self, url, title):
    self.request.session['uuid'] = str(self.object.id)
    context['template_title'] = title
    context['template_subtitle'] = 'alterar'
    context['template_url_delete'] = reverse_url('{}_delete'.format(url), [str(self.object.id)])
    context['template_url_active'] = reverse_url('{}_active'.format(url), [str(self.object.id)])
    context['template_form_fields'] = 'bluedata/template_form_render.html'
    context['template_btn_save'] = True
    context['template_buttons'] = [set_button('Voltar', reverse_url('{}_list'.format(url)), 'btn-outline-secondary',
                                              'la la-angle-left')]


# Seta o contexto do Delete
#
def set_context_delete(context, self, url, title):
    context['template_title'] = title
    context['template_subtitle'] = 'excluir'
    context['template_buttons'] = [set_button('Voltar', reverse_url('{}_update'.format(url), [str(self.object.id)]),
                                              'btn-outline-secondary', 'la la-angle-left')]


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



