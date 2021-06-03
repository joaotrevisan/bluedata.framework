from unicodedata import normalize

from django.urls import reverse
from django.utils.text import slugify


# Remove a acentuação da string
#
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


# Verifica se a URL existe
#
def reverse_url(url, args=None):
    try:
        if args:
            return reverse(url, args=args)
        else:
            return reverse(url)
    except Exception as ex:
        print(ex)
        return None


# cria o slug para qualquer model
#
def get_unique_slug(self, model_base):
    # recupera o modelo passado
    model = model_base.objects.model

    # verifica se o slug é o mesmo do banco
    obj = model.objects.filter(id=self.id).last()
    if obj:
        if obj.titulo.upper() == self.titulo.upper():
            return self.slug

    # preenche o novo slug
    str_to_slug = remover_acentos(self.titulo)
    unique_slug = slugify(str_to_slug)
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(unique_slug, num)
        num += 1

    return unique_slug
