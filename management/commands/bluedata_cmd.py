import os
import tempfile

from django.core.management.base import BaseCommand

from shutil import copyfile
import fileinput


class Command(BaseCommand):
    help = 'Cria os arquivos bases para um aplicação. ' \
           'python manage.py bluedata_cmd "app_path" "model_name" "base_url"'

    def add_arguments(self, parser):
        parser.add_argument('app_path', type=str)
        parser.add_argument('model_name', type=str)
        parser.add_argument('base_url', type=str)

    def handle(self, *args, **options):
        app_path = options['app_path']
        model_name = options['model_name']
        base_url = options['base_url']

        self.stdout.write('Starting process ...')

        try:
            self.stdout.write('app_path: {}'.format(app_path))
            self.stdout.write('model_name: {}'.format(model_name))
            self.stdout.write('base_url: {}'.format(base_url))

            # admin.py
            src = 'bluedata/templates/bluedata_modelos/admin.py'
            dst = '{}/admin.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

            # filters.py
            src = 'bluedata/templates/bluedata_modelos/filters.py'
            dst = '{}/filters.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

            # forms.py
            src = 'bluedata/templates/bluedata_modelos/forms.py'
            dst = '{}/forms.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

            # models.py
            src = 'bluedata/templates/bluedata_modelos/models.py'
            dst = '{}/models.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

            # urls.py
            src = 'bluedata/templates/bluedata_modelos/urls.py'
            dst = '{}/urls.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            replace_infile(dst, '[base_url]', base_url)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

            # views.py
            src = 'bluedata/templates/bluedata_modelos/views.py'
            dst = '{}/views.py'.format(app_path)
            copyfile(src, dst)
            replace_infile(dst, '[app_path]', app_path)
            replace_infile(dst, '[model_name]', model_name)
            replace_infile(dst, '[base_url]', base_url)
            delete_first(dst)
            self.stdout.write('>>> {} criado com sucesso'.format(dst))

        except Exception as ex:
            self.stdout.write('Erro ocorrido: {}'.format(ex))

        self.stdout.write('Ending process ...')


def replace_infile(dst, text_to_search, replacement_text):
    with fileinput.FileInput(dst, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


def delete_first(dst):
    with fileinput.FileInput(dst, inplace=True) as file:
        for line in file:
            if len(line[2:]) > 0:
                print(line[2:], end='')
            else:
                print(line[1:], end='')
