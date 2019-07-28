from django.db import models
import datetime


# Create your models here.


class Product(models.Model):
    sku = models.AutoField(primary_key=True, max_length=10, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class ItemHistory(models.Model):
    # datetime.date.today() seems to be coming out as "Mixed" in the mongodb. Maybe look to see if there are better
    # alternative identifiers
    date_bought = models.DateField(default=datetime.date.today(), null=False)
    date_sold = models.DateField(default=datetime.date.today(), null=False)

    def __datetime__(self):
        return self.date_bought
