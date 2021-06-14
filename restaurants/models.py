from django.utils.timezone import now
from django.db import models
from django.db.models.signals import pre_save, post_save
from .util import unique_slug_generator
from django.conf import settings


USER = settings.AUTH_USER_MODEL

# Create your models here.


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(USER, default=1)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=180, null=True, blank=True)
    category = models.CharField(max_length=180, null=True, blank=True)
    timestamp = models.DateTimeField(default=now, editable=False)
    Updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save(sender, instance, *args, **kwargs):
    print("saving...")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def rl_post_save(sender, instance, *args, **kwargs):
#     print("saving...")
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance.name)


pre_save.connect(rl_pre_save, sender=RestaurantLocation)

post_save.connect(rl_pre_save, sender=RestaurantLocation)
