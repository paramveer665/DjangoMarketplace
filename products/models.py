from django.db import models
from django.utils.text import slugify

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(blank=True,null=True)
    desc=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    active=models.BooleanField(default=True)
    featured=models.BooleanField()

    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}"
