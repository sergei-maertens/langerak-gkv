# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import langerak_gkv.users.models
import django.utils.timezone
from django.conf import settings
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('username', models.CharField(max_length=100, verbose_name='username', blank=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='last name', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sex', models.CharField(default=b'male', max_length=10, verbose_name='sex', blank=True, choices=[(b'male', 'male'), (b'female', 'female')])),
                ('address', models.CharField(help_text='Street name and number.', max_length=255, verbose_name='street', blank=True)),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal code', blank=True)),
                ('city', models.CharField(max_length=100, verbose_name='city', blank=True)),
                ('phone', models.CharField(help_text='Home phone number', max_length=20, verbose_name='phone', blank=True)),
                ('mobile', models.CharField(help_text='Mobile phone number', max_length=20, verbose_name='mobile phone number', blank=True)),
                ('birthdate', models.DateField(null=True, verbose_name='birth_date', blank=True)),
                ('picture', models.ImageField(help_text='Profile picture', upload_to=langerak_gkv.users.models.get_image_path, null=True, verbose_name='picture', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'picture', '400x300', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('about_me', models.TextField(help_text="Short 'about me' text", blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistrictFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.CharField(help_text='Describe what someone with this function does.', max_length=255, verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'district function',
                'verbose_name_plural': 'district functions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Last name of the householder.', max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'family',
                'verbose_name_plural': 'families',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_male', models.CharField(max_length=100, verbose_name='name (male)')),
                ('name_female', models.CharField(max_length=100, verbose_name='name (female)')),
                ('reverse_name_male', models.CharField(max_length=100, verbose_name='name (male)')),
                ('reverse_name_female', models.CharField(max_length=100, verbose_name='name (female)')),
                ('is_partner', models.BooleanField(default=False, verbose_name='is partner?')),
                ('is_child_parent', models.BooleanField(default=False, verbose_name='is child/parent?')),
                ('reverse', models.ForeignKey(to='users.RelationType', help_text='Reverse direction of the relation', null=True)),
            ],
            options={
                'verbose_name': 'relation type',
                'verbose_name_plural': 'relation types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation_type', models.ForeignKey(related_name='+', to='users.RelationType', help_text='User 2 is `relation type` of user 1.')),
                ('user1', models.ForeignKey(related_name='related_users', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='reverse_related_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user relation',
                'verbose_name_plural': 'user relations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(verbose_name='district', blank=True, to='users.District', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='district_function',
            field=models.ForeignKey(blank=True, to='users.DistrictFunction', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='family',
            field=models.ForeignKey(verbose_name='family', blank=True, to='users.Family', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='relations',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='users.UserRelation', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
