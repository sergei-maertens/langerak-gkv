from django.test import TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from .factories import UserFactory, UserRelationFactory, RelationTypeFactory
from ..models import UserRelation


class UserRelationTests(TestCase):

    def setUp(self):
        self.users = UserFactory.create_batch(2)

    def test_symmetrical_relation(self):
        """ Test that a symmetrical relation is created if one end is created """
        relation1 = UserRelationFactory.create(user1=self.users[0], user2=self.users[1])
        self.assertEqual(UserRelation.objects.count(), 2)
        relation2 = UserRelation.objects.filter(user1=self.users[1], user2=self.users[0]).get()
        self.assertEqual(relation1.relation_type, relation2.relation_type)

    def test_symmetrical_relation_updated(self):
        """ Test that updating one end syncs the other end """
        rel1 = UserRelationFactory.create(user1=self.users[0], user2=self.users[1])
        # rel2 is automatically created

        # set a new relation type
        new_type = RelationTypeFactory.create()
        rel1.relation_type = new_type
        rel1.save()

        # check the other end is updated
        rel2 = UserRelation.objects.get(user1=self.users[1], user2=self.users[0])
        self.assertEqual(rel2.relation_type, new_type)


class AdminTests(WebTest):
    def test_admin(self):
        """ Test that the symmetrical relation is created when adding relations through the admin """
        superuser = UserFactory.create(is_superuser=True, is_staff=True)

        relation_type = RelationTypeFactory.create()
        users = UserFactory.create_batch(2)

        admin = self.app.get(reverse('admin:users_user_change', args=[users[0].id]), user=superuser)
        form = admin.forms['user_form']
        form['user1_set-0-user2'] = users[1].pk
        form['user1_set-0-relation_type'] = relation_type.pk
        save = form.submit()
        self.assertRedirects(save, reverse('admin:users_user_changelist'))

        rel1 = UserRelation.objects.filter(user1=users[0], user2=users[1], relation_type=relation_type)
        rel2 = UserRelation.objects.filter(user1=users[1], user2=users[0], relation_type=relation_type)
        self.assertEqual(rel1.count(), 1)
        self.assertEqual(rel2.count(), 1)
