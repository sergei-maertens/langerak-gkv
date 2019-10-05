from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RelationType, UserRelation


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
    relation = kwargs.get("instance")
    if hasattr(relation, "skip_sync") and relation.skip_sync:
        return

    symm_relation, created = UserRelation.objects.get_or_create(
        user1=relation.user2,
        user2=relation.user1,
        defaults={"relation_type": relation.relation_type.reverse},
    )
    if not created and symm_relation.relation_type != relation.relation_type.reverse:
        symm_relation.relation_type = relation.relation_type.reverse
        symm_relation.skip_sync = True
        symm_relation.save()


@receiver(post_save, sender=RelationType)
def sync_reverse(sender, **kwargs):
    instance, created = kwargs.get("instance"), kwargs.get("created")
    fields = {
        "name_male": instance.reverse_name_male,
        "name_female": instance.reverse_name_female,
        "reverse_name_male": instance.name_male,
        "reverse_name_female": instance.name_female,
        "is_partner": instance.is_partner,
    }
    if created and not instance.reverse:
        instance.reverse = sender.objects.create(reverse=instance, **fields)
        instance.save()
    else:
        reverse, needs_save = instance.reverse, False
        for field_name, value in fields.items():
            if getattr(reverse, field_name) != value:
                setattr(reverse, field_name, value)
                needs_save = True
        if needs_save:
            reverse.save()
