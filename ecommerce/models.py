from django.db import models
from datetime import datetime , date

# Create your models here.

class Clothes(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics', default = None,null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
class Electronics(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics', default = None,null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
class Utencils(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics', default = None,null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
class Beauty_Products(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics', default = None,null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    