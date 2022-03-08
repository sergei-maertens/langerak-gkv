from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from django_webtest import WebTest

from ..models import RelationType, UserRelation
from .factories import RelationTypeFactory, UserFactory, UserRelationFactory


class UserRelationTests(TestCase):
    def setUp(self):
        self.users = UserFactory.create_batch(2)

    def test_reverse_relationtype_created(self):
        rel_type = RelationType.objects.create(
            name_male="Father",
            name_female="Mother",
            reverse_name_male="Son",
            reverse_name_female="Daughter",
            is_child_parent=True,
        )
        reverse_rel = rel_type.reverse
        self.assertIsNotNone(reverse_rel)

        self.assertEqual(reverse_rel.name_male, rel_type.reverse.name_male)
        self.assertEqual(reverse_rel.name_female, rel_type.reverse.name_female)
        self.assertEqual(rel_type.name_male, reverse_rel.reverse.name_male)
        self.assertEqual(rel_type.name_female, reverse_rel.reverse.name_female)
        self.assertEqual(reverse_rel.reverse, rel_type)

    def test_reverse_relationtype_updated(self):
        rel_type = RelationTypeFactory.create()
        rel_type.name_male = "changed this"
        rel_type.save()

        self.assertEqual(rel_type.reverse.reverse_name_male, "changed this")

    def test_symmetrical_relation(self):
        """Test that a symmetrical relation is created if one end is created"""
        relation1 = UserRelationFactory.create(user1=self.users[0], user2=self.users[1])
        self.assertEqual(UserRelation.objects.count(), 2)

        relation2 = UserRelation.objects.filter(
            user1=self.users[1], user2=self.users[0]
        ).get()
        self.assertEqual(relation2.relation_type, relation1.relation_type.reverse)
        self.assertEqual(relation2.relation_type.reverse, relation1.relation_type)

    def test_symmetrical_relation_updated(self):
        """Test that updating one end syncs the other end"""
        rel1 = UserRelationFactory.create(user1=self.users[0], user2=self.users[1])
        # rel2 is automatically created

        # set a new relation type
        new_type = RelationTypeFactory.create()
        rel1.relation_type = new_type
        rel1.save()

        # check the other end is updated
        rel2 = UserRelation.objects.get(user1=self.users[1], user2=self.users[0])
        self.assertEqual(rel2.relation_type, new_type.reverse)


class AdminTests(WebTest):
    def test_admin(self):
        """Test that the symmetrical relation is created when adding relations through the admin"""
        superuser = UserFactory.create(is_superuser=True, is_staff=True)

        relation_type = RelationTypeFactory.create()
        users = UserFactory.create_batch(2)

        admin = self.app.get(
            reverse("admin:users_user_change", args=[users[0].id]), user=superuser
        )
        form = admin.forms["user_form"]
        form["related_users-0-user2"] = str(users[1].pk)
        form["related_users-0-relation_type"] = str(relation_type.pk)
        save = form.submit()
        self.assertRedirects(save, reverse("admin:users_user_changelist"))

        rel1 = UserRelation.objects.filter(
            user1=users[0], user2=users[1], relation_type=relation_type
        )
        rel2 = UserRelation.objects.filter(
            user1=users[1], user2=users[0], relation_type=relation_type.reverse
        )
        self.assertEqual(rel1.count(), 1)
        self.assertEqual(rel2.count(), 1)
