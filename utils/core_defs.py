from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from apps.core.templatetags.core_tags import tag_acesso_menu


# CONTROLE DE ACESSO ***************************************************************************************************

# verifica se o usuário é ativo
# usuários superuser tem acesso normalmente
# necessário implementar para bluedata/view
#
def is_valid_user(usuario, access, error_list=[]):
    ret = True

    # usuário não existe
    if not usuario:
        ret = False
        error_list.append('Usuário não cadastrado no sistema')

    # superuser não precisa validar
    elif not usuario.is_superuser:

        # é usuário mas não está logado
        if usuario.is_anonymous:
            ret = False
            error_list.append('Usuário anônimo, faça login novamente')

        # é usuário inativo no sistema
        elif not usuario.is_active:
            ret = False
            error_list.append('Usuário inativo no sistema')

        # usuário tem acesso à página
        elif not tag_acesso_menu(usuario, access['menu'], access['item']):
            ret = False
            error_list.append('Usuário não tem acesso a essa página')

    return ret


# se inválido bloqueia acesso
# necessário implementar para bluedata/view
#
def set_dispatch(self, view):
    try:
        error_list = []
        if not is_valid_user(self.request.user, self.access, error_list):
            retorno = ''
            for item in error_list:
                retorno += item + '; '
            # raise Exception
            raise PermissionDenied(retorno)
        else:
            return super(view, self).dispatch(self.request)
    except Exception as e:
        print('>>> não possui acesso: {} {}'.format(self.access['action'], e))
        logout(self.request)
        return redirect('account_login')

# **********************************************************************************************************************
