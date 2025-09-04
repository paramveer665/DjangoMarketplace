from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=120)
    desc=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    active=models.BooleanField(default=True)
    featured=models.BooleanField()
