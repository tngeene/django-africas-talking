from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.forms.users import CustomAdminAuthenticationForm

User = get_user_model()

admin.site.site_header = "Django SMS App Admin"
admin.site.site_title = "Django SMS App"
admin.site.login_form = CustomAdminAuthenticationForm


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "role",
                    "gender",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    search_fields = (
        "first_name",
        "last_name",
        "role",
        "phone_number",
    )
    list_display = [
        "first_name",
        "last_name",
        "phone_number",
        "role",
        "gender",
        "is_active",
    ]
    list_filter = (
        "role",
        "gender",
    )


admin.site.register(User, CustomUserAdmin)
