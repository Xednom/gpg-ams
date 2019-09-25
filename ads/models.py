import uuid

from django.conf import settings
from django.db import models
from django.utils.timezone import now


class AdsContent(models.Model):
    STATUS = (
        ('Client Submitted to the Ad/s Writer', 'Client Submitted to the Ad/s Writer'),
        ('Ad/s Writer Processing', 'Ad/s Writer Processing'),
        ('Ad/s Content Completed', 'Ad/s Content Completed'),
        ('Ad/s Content Submitted to the Client', 'Ad/s Content Submitted to the Client'),
        ('Ad/s Content Closed', 'Ad/s Content Closed')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_requested = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True, default=now)
    date_completed = models.DateField(null=True, blank=True, default=now)
    client = models.ForeignKey(settings.CLIENTS, on_delete=models.PROTECT)
    apn_or_items_needs_ad_content = models.TextField(null=True, blank=True)
    client_recommendation = models.TextField(null=True, blank=True,
                                             help_text="Client's Recommendation of Ad Content Title(If the client wish to give)")
    content_instruction = models.TextField(null=True, blank=True,
                                           help_text="Ad/s Content instruction from the Client")
    content_finished = models.TextField(null=True, blank=True,
                                       help_text="Ad/s Content finished Ads(From the VA)")
    final_title = models.TextField(null=True, blank=True,
                                   help_text="Final title of the Add Content")
    modification = models.TextField(null=True, blank=True,
                                    help_text="Any Modification requested by the Client")
    content_status = models.CharField(max_length=150, choices=STATUS)
    ads_writer = models.ForeignKey(settings.STAFFS, on_delete=models.PROTECT)
    additional_notes = models.TextField(null=True, blank=True, help_text="Additional notes from the Ad/s writer")

    class Meta:
        ordering = ['-date_requested']

    def __str__(self):
        return '%s - %s' % (self.client, self.final_title)
