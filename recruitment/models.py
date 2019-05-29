import uuid
from django.db import models


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    educational_attainment = models.TextField(max_length=250)
    work_experience = models.CharField(max_length=150, null=True, blank=True)
    training_workshop_seminar_attended = models.TextField(null=True, blank=True)
    reference_contact = models.CharField(max_length=150, null=True, blank=True)
    communication_assessment = models.CharField(max_length=150, null=True, blank=True)
    technical_skills_assessment = models.CharField(max_length=150, null=True, blank=True)
    other_skills = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.name


class Reference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.PROTECT)
    reference_name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name