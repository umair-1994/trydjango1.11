from django.utils.timezone import now
from django.db import models


# Create your models here.


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=180, null=True, blank=True)
    category = models.CharField(max_length=180, null=True, blank=True)
    timestamp = models.DateTimeField(default=now, editable=False)
    Updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name