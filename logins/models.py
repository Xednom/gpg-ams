import uuid
from django.db import models

from fillables.models import VirtualAssistant


class Logins(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    type_of_apps = models.CharField(max_length=150, null=True, blank=True)
    link_to_the_app = models.URLField(null=True, blank=True)
    user_name = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    give_access_to = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'List of Logins of the client'
        verbose_name_plural = 'List of Logins of the clients'
        ordering = ['client_full_name']

    def __str__(self):
        return str(self.client_full_name)