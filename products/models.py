from django.db import models
from django.db.models import Model


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=10.00)
    image = models.FileField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def ProductListView(self):
        return self.title
