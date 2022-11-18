from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": _(
            "Please enter the correct %(username)s or email and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }

    username = UsernameField(
        label="Email/Phone number",
        widget=forms.TextInput(attrs={"autofocus": True}),
    )
