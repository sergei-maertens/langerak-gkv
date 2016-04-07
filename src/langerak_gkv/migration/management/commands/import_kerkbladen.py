import os

from django.core.files import File as _File
from django.core.management import BaseCommand
from django.db import transaction

from cms.api import add_plugin
from cms.models import Page
from filer.models import File, Folder

from ...models import Document


CAT_KERKBLADEN = 41


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('page_slug')
        parser.add_argument('dir')
        parser.add_argument('--placeholder', default='page_content')

    def handle(self, **options):
        language, plugin_type = 'nl', 'FilerFilePlugin'
        page = Page.objects.get(title_set__slug=options['page_slug'], publisher_is_draft=True)
        placeholder = page.placeholders.get(slot=options['placeholder'])

        folder, _ = Folder.objects.get_or_create(name='Kerkbladen', parent=None)
        files_dir = os.path.abspath(options['dir'])

        documents = Document.objects.using('legacy').filter(catid=CAT_KERKBLADEN)
        with transaction.atomic():
            for document in documents:
                pdf = os.path.join(files_dir, document.dmfilename)
                filemodel = File(folder=folder)
                with open(pdf, 'r') as _pdf:
                    filemodel.file.save(os.path.split(pdf)[1], _File(_pdf))
                data = {
                    'title': document.dmname,
                    'file': filemodel,
                    'target_blank': True,
                }
                add_plugin(placeholder, plugin_type, language, **data)
