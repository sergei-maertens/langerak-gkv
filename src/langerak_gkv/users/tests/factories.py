import factory
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user-{n}")
    first_name = factory.fuzzy.FuzzyChoice(["John", "Jane"])
    last_name = "Doe"
    email = factory.LazyAttributeSequence(
        lambda a, n: "{0}.{1}-{2}@example.com".format(
            a.first_name.lower(), a.last_name.lower(), n
        )
    )
    password = factory.PostGenerationMethodCall("set_password", "secret")

    class Meta:
        model = "users.User"
