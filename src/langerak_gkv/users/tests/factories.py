import factory
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.User"

    first_name = factory.fuzzy.FuzzyChoice(["John", "Jane"])
    last_name = "Doe"
    email = factory.LazyAttributeSequence(
        lambda a, n: "{0}.{1}-{2}@example.com".format(
            a.first_name.lower(), a.last_name.lower(), n
        )
    )
    password = factory.PostGenerationMethodCall("set_password", "secret")


class RelationTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.RelationType"

    name_male = factory.fuzzy.FuzzyChoice(["Vader", "Vriend"])
    name_female = factory.fuzzy.FuzzyChoice(["Moeder", "Vriendin"])

    reverse_name_male = factory.fuzzy.FuzzyChoice(["Zoon", "Vriend"])
    reverse_name_female = factory.fuzzy.FuzzyChoice(["Dochter", "Vriendin"])

    is_partner = factory.fuzzy.FuzzyChoice([False, True])
    is_child_parent = factory.fuzzy.FuzzyChoice([True, False])


class UserRelationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.UserRelation"

    user1 = factory.SubFactory(UserFactory)
    user2 = factory.SubFactory(UserFactory)
    relation_type = factory.SubFactory(RelationTypeFactory)
