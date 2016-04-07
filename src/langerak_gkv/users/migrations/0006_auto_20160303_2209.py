# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_add_family_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='member_type',
            field=models.CharField(blank=True, max_length=20, verbose_name='member type', choices=[(b'baptised', 'baptised member'), (b'practicing', 'practicing member'), (b'guest', 'guest member')]),
        ),
        migrations.AlterField(
            model_name='relationtype',
            name='reverse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.RelationType', help_text='Reverse direction of the relation', null=True),
        ),
        migrations.AlterField(
            model_name='relationtype',
            name='reverse_name_female',
            field=models.CharField(max_length=100, verbose_name='reverse name (female)'),
        ),
        migrations.AlterField(
            model_name='relationtype',
            name='reverse_name_male',
            field=models.CharField(max_length=100, verbose_name='reverse name (male)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='district', blank=True, to='users.District', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='district_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='users.DistrictFunction', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='family', blank=True, to='users.Family', null=True),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='relation_type',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, to='users.RelationType', help_text='User 2 is `relation type` of user 1.'),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='user1',
            field=models.ForeignKey(related_name='related_users', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='user2',
            field=models.ForeignKey(related_name='reverse_related_users', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
