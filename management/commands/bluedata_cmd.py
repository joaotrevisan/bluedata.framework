import os
import fileinput

from django.core.management.base import BaseCommand
from shutil import copyfile


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
            self.stdout.write('xxx')

            # admin.py
            create_file(self, 'admin', app_path, model_name, base_url)

            # filters.py
            create_file(self, 'filters', app_path, model_name, base_url)

            # forms.py
            create_file(self, 'forms', app_path, model_name, base_url)

            # models.py
            create_file(self, 'models', app_path, model_name, base_url)

            # urls.py
            create_file(self, 'urls', app_path, model_name, base_url)

            # views.py
            create_file(self, 'views', app_path, model_name, base_url)

        except Exception as ex:
            self.stdout.write('Erro ocorrido: {}'.format(ex))

        self.stdout.write('Ending process ...')


def create_file(self, file, app_path, model_name, base_url):
    try:
        src = 'bluedata/templates/bluedata_modelos/{}.py'.format(file)
        dst = '{}/{}.py'.format(app_path, file)
        bkp = '{}/_{}.py'.format(app_path, file)

        # backup do arquivo original
        if os.path.isfile(dst):
            copyfile(dst, bkp)
            self.stdout.write('>>> backup: {}'.format(bkp))

        # substitui por modelo
        if os.path.isfile(src):
            copyfile(src, dst)
            self.stdout.write('>>> overwrite: {}'.format(dst))

        # altera as chaves nos arquivos
        replace_infile(dst, '[app_path]', app_path.replace('/', '.'))
        replace_infile(dst, '[model_name]', model_name)
        replace_infile(dst, '[base_url]', base_url)

        # # remove a linha de comentário
        delete_first(dst)

        # sucesso
        self.stdout.write('>>> {} criado com sucesso'.format(dst))
        self.stdout.write('xxx')

    except Exception as e:
        print(e)


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
