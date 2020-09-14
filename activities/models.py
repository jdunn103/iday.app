from common.models import IdayModel
from django.db import models
from django.utils import timezone
from django.urls import reverse

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

class Event(IdayModel):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True)
    activity = models.ForeignKey('Activity', on_delete=models.PROTECT, related_name='events')

    @property
    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return None

    def get_absolute_url(self):
        return reverse('event-update', args=[str(self.slug)])
        
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.activity.name + '-' + str(self.start_time)