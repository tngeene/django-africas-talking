from django.contrib.auth import get_user_model
from django.db import models

from core.constants import SMS_STATUS_CODE_CHOICES

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = "-created_at"


class ShortMessageManager(models.Manager):
    def save_from_response(self, response, message, user=None, *args):
        response_message = response["SMSMessageData"]["Message"]
        status_code = response["SMSMessageData"]["Recipients"][0][
            "statusCode"
        ]
        phone_number = response["SMSMessageData"]["Recipients"][0]["number"]
        cost = response["SMSMessageData"]["Recipients"][0]["cost"]
        status = response["SMSMessageData"]["Recipients"][0]["status"]
        message_id = response["SMSMessageData"]["Recipients"][0]["messageId"]

        saved_message = self.create(
            response_message=response_message,
            status_code=status_code,
            phone_number=phone_number,
            cost=cost,
            status=status,
            message_id=message_id,
            message=message,
        )

        if user:
            saved_message.recipient = user
            saved_message.save()
            saved_message.refresh_from_db()

        return saved_message


class ShortMessage(models.Model):
    message = models.TextField()
    response_message = models.TextField()
    status_code = models.CharField(
        max_length=60, choices=SMS_STATUS_CODE_CHOICES
    )
    phone_number = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    message_id = models.CharField(max_length=100)
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="messages_received",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ShortMessageManager()

    def __str__(self):
        return f"{self.recipient} {self.status} on {self.created_at}"
