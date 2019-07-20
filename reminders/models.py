import uuid

from django.db import models
from django.urls import reverse

from users.models import Clients, Staffs

class ManagerReminders(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Processing', 'Processing'),
        ('In Review', 'In Review'),
        ('Completed', 'Completed'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    additional_comment = models.TextField(null=True, blank=True)
    requestor = models.CharField(max_length=150, null=True, blank=True)
    requestee = models.CharField(max_length=150, null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    memo_from_requestor = models.TextField()
    memo_from_requestee = models.TextField(default="Memo will be in a minute or two.", null=True, blank=True)
    comment_from_admin = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.requestor
    
    def get_absolute_url(self):
        return reverse('reminders:view-reminders')

    class Meta:
        verbose_name = 'General Reminder'
        verbose_name_plural = 'General Reminders'
        ordering=['-date']
