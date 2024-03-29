from django import forms
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from image_cropping import ImageCropWidget as AdminImageCropWidget

from .models import User
from .widgets import ImageCropWidget


class UserCreationForm(forms.ModelForm):

    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {"password_mismatch": _("The two password fields didn't match.")}
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."),
    )
    username = forms.CharField(
        label=_("Username"), required=True, help_text=_("Used for login.")
    )

    class Meta:
        model = User
        fields = "__all__"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"], code="password_mismatch"
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email"), max_length=254, required=False)
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = User
        fields = "__all__"
        widgets = {"picture": AdminImageCropWidget}

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get("user_permissions", None)
        if f is not None:
            f.queryset = f.queryset.select_related("content_type")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username:
            duplicates = User._default_manager.filter(username=username).exclude(
                pk=self.instance.pk
            )
            if duplicates.exists():
                raise forms.ValidationError(
                    _("This username is taken, choose a different username.")
                )
        return username


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "mobile",
            "picture",
            "cropping",
            "about_me",
        )
        widgets = {"picture": ImageCropWidget}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username:
            duplicates = User._default_manager.filter(username=username).exclude(
                pk=self.instance.pk
            )
            if duplicates.exists():
                raise forms.ValidationError(
                    _("This username is taken, choose a different username.")
                )
        return username


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label=_("Username"))
