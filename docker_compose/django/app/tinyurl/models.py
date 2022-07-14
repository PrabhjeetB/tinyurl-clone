from django.conf import settings
from django.db import models
from django.urls import reverse_lazy

from model_utils.models import TimeStampedModel


class TinyUrl(TimeStampedModel):
    """
    TinyUrl object
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=10, primary_key=True)
    original_url = models.CharField(max_length=100, blank=False)

    def get_absolute_url(self):
        return reverse_lazy("tinyurl:tiny-list")
