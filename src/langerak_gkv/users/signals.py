from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserRelation


@receiver(post_save, sender=UserRelation)
def sync_user_relations(sender, **kwargs):
    """
    Users have assymetrical m2m relations with other users through a
    `UserRelation` model. This signal handler syncs it to keep some sort of
    symmetry.

    Whenever a UserRelation with `user1` and `user2` is created, a swapped (
    user1 and user2) relation is created/updated to show the relations for both
    ends.
    """
    relation = kwargs.get('instance')
    if hasattr(relation, 'skip_sync') and relation.skip_sync:
        return

    symm_relation, created = UserRelation.objects.get_or_create(
        user1=relation.user2, user2=relation.user1,
        defaults={
            'relation_type': relation.relation_type
        }
    )
    if not created and symm_relation.relation_type != relation.relation_type:
        symm_relation.relation_type = relation.relation_type
        symm_relation.skip_sync = True
        symm_relation.save()
