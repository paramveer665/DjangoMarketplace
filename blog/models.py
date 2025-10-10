from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    blogtitle=models.CharField(max_length=200,null=False,blank=False)
    content=models.TextField(max_length=2500,null=True,blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blogs",null=False,blank=False)
    publishedAt=models.DateTimeField( blank=True,default=now())



    def __str__(self):
        return f"{self.blogtitle}"

