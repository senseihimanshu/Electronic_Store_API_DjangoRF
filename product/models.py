from django.conf import settings
from django.db import models


def upload_product_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to=upload_product_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return str(self.name)[:50]
