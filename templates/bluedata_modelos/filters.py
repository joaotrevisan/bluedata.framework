# import django_filters
#
# from [app_path].models import [model_name]
#
#
# class [model_name]Filter(django_filters.FilterSet):
#     ORDER_BY = (('decrescente', 'Mais recentes'), ('crescente', 'Mais antigos'))
#     ordering = django_filters.ChoiceFilter(label='Ordenar Início', choices=ORDER_BY, method='order_by')
#
#     class Meta:
#         model = [model_name]
#         fields = {
#             'titulo': ['icontains'],
#         }
#
#     # label do filtro no template
#     def __init__(self, *args, **kwargs):
#         super([model_name]Filter, self).__init__(*args, **kwargs)
#         self.filters['titulo__icontains'].label = "Título"
#
#     # ordena a lista filtrada
#     def order_by(self, queryset, name, value):
#         expression = 'data_criacao' if value == 'crescente' else '-data_criacao'
#         return queryset.order_by(expression)
