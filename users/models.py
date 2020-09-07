from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.urls import reverse
from activities.models import Event

class CustomUser(AbstractUser):
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)

    @property
    def is_busy(self):
        return Event.objects.filter(Q(end_time__isnull=True) & Q(start_time__isnull=False))

    def get_absolute_url(self):
        return reverse('my-account')
