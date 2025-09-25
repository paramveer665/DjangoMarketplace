from django.contrib import admin

# Register your models here.
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display=('title','slug','price','active','featured')

admin.site.register(Products,ProductsAdmin)

