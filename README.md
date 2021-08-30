# bluedata.app
Componente bluedata: App


# REQUISITOS

Incluir a pasta "bluedata" na raiz do projeto
git submodule add https://github.com/joaotrevisan/bluedata.framework.git bluedata

O template principal (/templates) deve chamar "keen.html"
O nome do template pode ser sobrescrito em set_context_[list, create, update, delete], através da variável context['template']


# INSTALAÇÃO

[instalar] pip install django-filter

SETTINGS.PY

INSTALLED_APPS = [
...
'bluedata'
...
]

ADICIONAR NO TEMPLATE PRINCIPAL

<!--begin::Buedata Style-->
<style>{% include 'bluedata_static/style.css' %}</style>
<!--end::Buedata Style-->

<!--begin::Buedata Style-->
<script>{% include 'bluedata_static/script.js' %}</script>
<!--end::Buedata Style-->


# AUTOMAÇÃO

CRIANDO O NOVO APP
python manage.py startapp APP_NAME

RODANDO AUTOMAÇÃO
python manage.py bluedata_cmd "apps/aluno" "Aluno" "aluno"
