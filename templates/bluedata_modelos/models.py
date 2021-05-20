# import uuid
#
# from django.db import models
#
# from bluedata.helpers import get_unique_slug
#
#
# class [model_name](models.Model):
#     # uuid
#     id = models.UUIDField(
#         primary_key=True, unique=True, default=uuid.uuid4, editable=False)
#     # texto slug
#     slug = models.SlugField(
#         max_length=250, blank=True, null=True, unique=True, editable=False)
#     # texto da tag
#     descricao = models.CharField(
#         max_length=255, verbose_name='Descrição')
#     # exibe ou não
#     is_active = models.BooleanField(
#         default=True, verbose_name='Ativo')
#
#     # data criacao
#     data_criacao = models.DateTimeField(
#         editable=False, auto_now_add=True, null=True, blank=True)
#     # data atualizacao
#     data_alteracao = models.DateTimeField(
#         editable=False, auto_now=True, null=True, blank=True)
#
#     class Meta:
#         verbose_name = '[model_name]'
#         verbose_name_plural = '[model_name]s'
#         ordering = ['-is_active', 'descricao']
#
#     def save(self, *args, **kwargs):
#         self.slug = get_unique_slug(self, [model_name])
#         super([model_name], self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.descricao
