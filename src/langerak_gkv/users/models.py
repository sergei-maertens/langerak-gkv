import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from djchoices import DjangoChoices, ChoiceItem


class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Sex(DjangoChoices):
        male = ChoiceItem('male', _('male'))
        female = ChoiceItem('female', _('female'))

    def get_image_path(instance, filename):
        """
        Keep the pictures in folders directly relate to the user:
        /media/images/users/<user_id>/example.jpg
        """
        name, extension = os.path.splitext(filename)
        filename = name + extension
        return os.path.join('images/users', str(instance.id), filename)

    email = models.EmailField(_('email address'), max_length=254, unique=True)

    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # profile related
    sex = models.CharField(_('sex'), max_length=10, blank=True, choices=Sex.choices, default=Sex.male)
    address = models.CharField(_('street'), max_length=255, blank=True,
        help_text=_('Street name and number.'))
    postal_code = models.CharField(_('postal code'), max_length=10, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)

    phone = models.CharField(_('phone'), max_length=20, blank=True,
        help_text=_('Home phone number'))
    mobile = models.CharField(_('mobile phone number'), max_length=20, blank=True,
        help_text=_('Mobile phone number'))

    birthdate = models.DateField(_('birth_date'), blank=True, null=True)
    picture = models.ImageField(_('picture'), upload_to=get_image_path,
        blank=True, null=True, help_text=_('Profile picture'))

    # district/family information
    district = models.ForeignKey('users.District', verbose_name=_(u'district'),
        blank=True, null=True)
    district_function = models.ForeignKey('users.DistrictFunction', blank=True, null=True)
    family = models.ForeignKey('users.Family', verbose_name=_('family'), blank=True, null=True)
    relations = models.ManyToManyField('self', blank=True, null=True,
        through='users.UserRelation', symmetrical=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def get_postal_code(self):
        """ Format the postal code: 3118BJ becomes 3118 BJ """ # TODO: test
        if not self.postal_code:
            return None
        bits = self.postal_code.split(' ')
        if len(bits) == 1: # there was no space
            bits = [bits[:4], bits[4:]]
        return "{0} {1}".format(bits[0], bits[1])

    @property
    def relations(self):
        sr = ('user1', 'user2', 'relation_type')
        qs1 = self.user1_set.select_related(*sr).all()
        qs2 = self.user2_set.select_related(*sr).all()
        return qs1 | qs2

    @cached_property
    def partner(self):
        qs = self.relations.filter(relation_type__is_partner=True)
        if qs.exists():
            relation = qs.get()
            # check the side of the relation
            if relation.user1 == self:
                return relation.user2
            return relation.user1
        return None


class UserRelation(models.Model):
    """
    E.g. user2 is daughter, user1 is father, relation type is 'daughter'
    """
    user1 = models.ForeignKey('users.User', related_name='user1_set')
    user2 = models.ForeignKey('users.User', related_name='user2_set')
    relation_type = models.ForeignKey('users.RelationType',
        help_text=_('User 2 is `relation type` of user 1.'))

    class Meta:
        verbose_name = _(u'user relation')
        verbose_name_plural = _(u'user relations')

    def __unicode__(self):
        return u"{user2} ({user2_relation} of {user1})".format(**self.get_textual_repr())

    def get_textual_repr(self):
        """ Does the logic in checking the sexes and displaying the correct relation """
        s1_attr = 'name_%s' % self.user1.sex
        s2_attr = 'name_%s' % self.user2.sex

        return {
            'user1': self.user1.get_full_name(),
            'user2': self.user2.get_full_name(),
            'user1_relation': getattr(self.relation_type, s1_attr),
            'user2_relation': getattr(self.relation_type, s2_attr),
        }


class RelationType(models.Model):
    name = models.CharField(_('name (generic)'), max_length=100)
    name_male = models.CharField(_('name (male)'), max_length=100)
    name_female = models.CharField(_('name (female)'), max_length=100)
    name_reverse_male = models.CharField(_('name reverse (male)'), max_length=100,
        help_text=_('Name for the reverse relation, e.g. Father and daugther.'))
    name_reverse_female = models.CharField(_('name reverse (female)'), max_length=100,
        help_text=_('Name for the reverse relation, e.g. parent and child.'))
    is_partner = models.BooleanField(_('is partner?'), default=False)

    class Meta:
        verbose_name = _(u'relation type')
        verbose_name_plural = _(u'relation types')

    def __unicode__(self):
        return self.name


class District(models.Model):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _(u'district')
        verbose_name_plural = _(u'districts')

    def __unicode__(self):
        return self.name


class DistrictFunction(models.Model):
    name = models.CharField(_('name'), max_length=255)
    description = models.CharField(_('description'), max_length=255, blank=True,
        help_text=_('Describe what someone with this function does.'))

    class Meta:
        verbose_name = _(u'district function')
        verbose_name_plural = _(u'district functions')

    def __unicode__(self):
        return self.name


class Family(models.Model):
    """ A family groups members living together in the same physical house. """
    name = models.CharField(_('name'), max_length=255,
        help_text=_('Last name of the householder.'))

    class Meta:
        verbose_name = _(u'family')
        verbose_name_plural = _(u'families')

    def __unicode__(self):
        return _('Fam. {name}').format(name=self.name)





# Profielpagina
# -Overzichtspagina van alle gemeenteleden onder elkaar met thumbnail foto en kort overzicht belangrijkste contactgegevens
#     Uitgebreide zoekfunctionaliteit
# -Persoonlijke pagina met volgende gegevens:
# Eerstegraads connecties (in kleine thumbnails)

