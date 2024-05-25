from django.db import models
import uuid
import secrets

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=50, default=secrets.token_urlsafe)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.account_name
