import os
import re

from django.core.management.base import NoArgsCommand

from langerak_gkv.migration.models import Event, Category
from langerak_gkv.liturgies.models import Liturgy, Service
from langerak_gkv.activities.models import Activity, ActivityType


CAT_KERKDIENST = 2
CAT_TYPE_MAPPING = {}


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        # map categories to types
        n_created = 0
        for category in Category.objects.using('legacy').all():
            type_, created = ActivityType.objects.get_or_create(
                name__iexact=category.cat_name,
                defaults={'name': category.cat_name}
            )
            CAT_TYPE_MAPPING[category] = type_
            if created:
                n_created += 1

        self.stdout.write('Created %d activity types' % n_created)

        self.stdout.write('Migrating events...')

        collecte_regex = re.compile(r'(collecte [123]:?(?P<collecte>[\w \-]+))+', re.IGNORECASE)
        audio_field = field = Liturgy._meta.get_field_by_name('audiofile')[0]
        upload_to = audio_field.upload_to

        events = Event.objects.using('legacy').all()
        for event in events:
            start = event.start_date.date()
            if event.category_id == CAT_KERKDIENST:
                start_time = event.start_date.time()
                service, _ = Service.objects.get_or_create(
                    time=start_time,
                    defaults={'name': start_time.strftime('%H:%i%s')}
                )

                init_kwargs = {
                    'date': start,
                    'service': service,
                    'preach_author': event.preekvan or '',
                    'main_section': event.bijbelgedeelte or '',
                    'main_chapter': event.hoofdstuk or '',
                    'main_verse': event.vers or '',
                    'service_theme': (event.thema or '')[:255],
                    'liturgy': event.liturgiebord or '',
                    'audiofile': '',
                    'beamist': event.beamist or '',
                    'organist': event.organist or '',
                    'extra_information': u"{}\n{}".format(event.contact, event.email),
                }
                results = collecte_regex.findall(event.description)
                for i, match in enumerate(results):
                    j = i + 1
                    init_kwargs['collection_goal%d' % j] = match[1]

                if event.preekvan:
                    if event.preekvan in event.description:
                        init_kwargs['preacher'] = event.preekvan
                    else:
                        self.stdout.write('Check event %d for preacher' % event.pk)

                if event.geluid:
                    init_kwargs['audiofile'] = os.path.join(upload_to, event.geluid)

                try:
                    Liturgy.objects.create(**init_kwargs)
                except Exception as e:
                    import bpdb; bpdb.set_trace()
            else:
                import bpdb; bpdb.set_trace()
                Activity.objects.create(
                    name=event.title,
                    start_date=start,
                    end_date=event.end_date.date() if event.end_date else start,
                    start_time=event.start_date.time(),
                    end_time=event.end_date.time() if event.end_date else None
                )


        raise TypeError('blah')
