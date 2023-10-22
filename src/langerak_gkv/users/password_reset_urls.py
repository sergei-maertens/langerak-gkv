from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

urlpatterns = [
    # request a password reset
    path(
        "recover/",
        PasswordResetView.as_view(
            email_template_name="password_reset/recovery_email.txt",
            subject_template_name="password_reset/recovery_email_subject.txt",
            template_name="password_reset/recovery_form.html",
            success_url=reverse_lazy("user_passwords:password_reset_done"),
        ),
        name="password_reset",
    ),
    # confirmation that a reset email is sent
    path(
        "recover/done/",
        PasswordResetDoneView.as_view(
            template_name="password_reset/reset_sent.html",
        ),
        name="password_reset_done",
    ),
    # form to configure new password
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="password_reset/reset.html",
            success_url=reverse_lazy("user_passwords:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    # confirmation that password reset is completed
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="password_reset/recovery_done.html",
        ),
        name="password_reset_complete",
    ),
]
