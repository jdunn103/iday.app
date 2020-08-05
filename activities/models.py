from common.models import IdayModel
from django.db import models

from common.utils.text import unique_slug

from django.conf import settings

class Activity(IdayModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        
        super().save(*args, **kwargs)

    
    class Meta:
        verbose_name_plural = 'Activities'