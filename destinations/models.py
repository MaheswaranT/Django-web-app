from django.db import models
from accounts.models import Account

class Destination(models.Model):
    account = models.ForeignKey(Account, related_name='destinations', on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=6, choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')])
    headers = models.JSONField()

    def __str__(self):
        return f'{self.account.account_name} - {self.url}'
