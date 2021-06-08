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
#     template_title = '[model_name]s'
#     access = {'menu': 'Sistema', 'item': '[model_name]', 'action': 'list'}
#     fields = [
#         {'field': 'id', 'type': 'CharField', 'verbose': '#'},
#         {'field': 'titulo', 'type': 'CharField', 'verbose': 'Título'},
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
#     access = {'menu': 'Sistema', 'item': '[model_name]', 'action': 'create'}
#
#
# # Update
# #
# class [model_name]Update(BaseUpdateView):
#     model = [model_name]
#     form_class = [model_name]Form
#     base_url = '[base_url]'
#     template_title = '[model_name]'
#     access = {'menu': 'Sistema', 'item': '[model_name]', 'action': 'update'}
#
#
# # Delete
# #
# class [model_name]Delete(BaseDeleteView):
#     model = [model_name]
#     base_url = '[base_url]'
#     template_title = '[model_name]'
#     access = {'menu': 'Sistema', 'item': '[model_name]', 'action': 'delete'}
#
#
# # ToggleActive
# #
# class [model_name]Active(BaseActiveView):
#     model = [model_name]
#     base_url = '[base_url]'
#     access = {'menu': 'Sistema', 'item': '[model_name]', 'action': 'active'}
