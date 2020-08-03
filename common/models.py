from django.db import models

class IdayModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )

    class Meta:
        abstract = True