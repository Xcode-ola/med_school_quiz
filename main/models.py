from django.db import models

# Create your models
class contact_detail(models.Model):
    telephone = models.CharField(max_length=20, blank=True, null=True)
    telephone2 = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)