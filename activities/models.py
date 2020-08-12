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
    
    def __str__(self):
        return self.user.username + '-' + self.name
    
    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['name']

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.ForeignKey('Activity', on_delete=models.PROTECT, related_name='events')

    @property
    def duration(self):
        return self.end_time - self.start_time