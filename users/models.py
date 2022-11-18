from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.utils import format_phone_number
from users import constants as user_constants


class UserAccountManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            models.Q(**{self.model.USERNAME_FIELD: username})
            | models.Q(**{self.model.EMAIL_FIELD: username})
        )

    # override create user method to accept email and phone number as username
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(
            username=extra_fields.get("phone_number"),
            email=email,
            password=password,
            **extra_fields,
        )

    # override createsuperuser method to accept email and phone number as username
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(
            username=extra_fields.get("phone_number"),
            email=email,
            password=password,
            **extra_fields,
        )


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    role = models.CharField(
        max_length=30,
        choices=user_constants.ROLE_CHOICES,
        default="customer",
    )
    gender = models.CharField(
        max_length=10, choices=user_constants.GENDER_CHOICES
    )
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
    ]
    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = "email"

    objects = UserAccountManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.get_full_name()

    def save_phone_number(self, phone_number: str):
        self.phone_number = format_phone_number(phone_number)
        self.save()
