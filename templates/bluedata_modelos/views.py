# from bluedata.views import BaseCreateView, BaseListView, BaseUpdateView, BaseDeleteView, BaseActiveView
#
# from [app_path].filters import [model_name]Filter
# from [app_path].forms import [model_name]Form
# from [app_path].models import [model_name]
#
#
# # List
# #
# class [model_name]List(BaseListView):
#     model = [model_name]
#     filterset_class = [model_name]Filter
#     base_url = '[base_url]'
#     template_title = 'Lista de [model_name]s'
#     fields = [
#         {'field': 'id', 'type': 'IntegerField', 'verbose': '#'},
#         {'field': 'descricao', 'type': 'CharField', 'verbose': 'Descrição'},
#         {'field': 'is_active', 'type': 'BooleanField', 'verbose': 'Ativo?'},
#     ]
#
#
# # Create
# #
# class [model_name]Create(BaseCreateView):
#     model = [model_name]
#     form_class = [model_name]Form
#     base_url = '[base_url]'
#     template_title = '[model_name]'
#
#
# # Update
# #
# class [model_name]Update(BaseUpdateView):
#     model = [model_name]
#     form_class = [model_name]Form
#     base_url = '[base_url]'
#     template_title = '[model_name]'
#
#
# # Delete
# #
# class [model_name]Delete(BaseDeleteView):
#     model = [model_name]
#     base_url = '[base_url]'
#     template_title = '[model_name]'
#
#
# # ToggleActive
# #
# class [model_name]Active(BaseActiveView):
#     model = [model_name]
#     base_url = '[base_url]'
