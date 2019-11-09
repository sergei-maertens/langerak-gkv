from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned


class EmailModelBackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL, but also
    looks at the email of the user.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        if not username:
            return None

        UserModel = get_user_model()
        try:
            user = UserModel._default_manager.get(email=username)
            if user.check_password(password):
                return user
        # e-mail addresses can be duplicated
        except (UserModel.DoesNotExist, MultipleObjectsReturned):
            return None
