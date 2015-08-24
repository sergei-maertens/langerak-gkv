from import_export import resources

from .models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 'is_active',
            'sex', 'address', 'postal_code', 'city', 'phone', 'mobile',
            'birthdate'
        )
