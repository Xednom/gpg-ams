import uuid

from django.db import models


class ManagerReminders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    manager_under = models.CharField(max_length=150, null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=150, null=True, blank=True)
    notes_from_company = models.TextField()
    notes_from_manager = models.TextField()

    def __str__(self):
        return self.manager_under

    class Meta:
        verbose_name = 'Manager Reminder'
        verbose_name_plural = 'Manager Reminders'
        ordering=['-date']
