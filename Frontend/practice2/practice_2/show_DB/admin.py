from django.contrib import admin

# Register your models here.
from .models import Product, ItemHistory

admin.site.register(Product)
admin.site.register(ItemHistory)