import uuid
from django.db import models
from django.conf import settings

from fillables.models import VirtualAssistant


class Logins(models.Model):
    COMPANY_CATEGORY = (
        ('landmaster.us', 'landmaster.us'),
        ('gpgcorporations.com', 'gpgcorporations.com'),
        ('callme.com.ph', 'callme.com.ph'),
        ('virtualExpressServices.com', 'virtualExpressServices.com'),
        ('creatif-designs.com', 'creatif-designs.com'),
        ('vacantpropertiesglobal.com', 'vacantpropertiesglobal.com')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_full_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    company_category = models.CharField(max_length=150, choices=COMPANY_CATEGORY, null=True, blank=True)
    apps_url_link = models.URLField(null=True, blank=True)
    type_of_apps = models.CharField(max_length=150, null=True, blank=True)
    link_to_the_app = models.URLField(null=True, blank=True)
    user_name = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    give_access_to = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)
    date_created = models.DateField(auto_now_add=True)
    added_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'General Login'
        verbose_name_plural = 'General Logins'
        ordering = ['client_full_name']

    def __str__(self):
        return str(self.client_full_name)
