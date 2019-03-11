import eav
from django.db import models


class ClientName(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class CallDetails(models.Model):
    client_name = models.ForeignKey(ClientName, on_delete=models.PROTECT, null=True, blank=True, db_index=True)
    letter_info = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.client_name)

    class Meta:
        verbose_name = 'Call Detail'
        ordering = ['client_name']


eav.register(ClientName)
eav.register(CallDetails)