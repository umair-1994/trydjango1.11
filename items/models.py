import now as now
from django.db import models
from django.conf import settings
from restaurants.models import RestaurantLocation
from django.utils.timezone import now
# Create your models here.

USERS = settings.AUTH_USER_MODEL


class Item(models.Model):

    user = models.ForeignKey(USERS)
    restaurant = models.ForeignKey(RestaurantLocation)

    name = models.CharField(max_length=100)
    contents = models.TextField(help_text='Enter comma separated names')
    excludes = models.TextField(help_text='Enter comma separated names', null=True, blank=True)
    timestamp = models.DateTimeField(default=now, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated_date', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

