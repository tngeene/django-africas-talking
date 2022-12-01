from allauth.account import app_settings as allauth_app_settings
from allauth.account.app_settings import AuthenticationMethod
from allauth.account.forms import LoginForm
from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext


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


class CustomDashboardAuthenticationForm(LoginForm):
    # override allauth custom form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        assert (
            allauth_app_settings.AUTHENTICATION_METHOD
            == AuthenticationMethod.USERNAME_EMAIL
        )
        login_widget = forms.TextInput(
            attrs={
                "placeholder": _("Enter your email address or phone number"),
                "autocomplete": "email",
            }
        )
        login_field = forms.CharField(
            label=pgettext("field label", "Email/Phone Number"),
            widget=login_widget,
        )
        self.fields["login"] = login_field
