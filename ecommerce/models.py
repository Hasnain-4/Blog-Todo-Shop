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

# Save Product Details...................

class ProductDetail(models.Model):
    ortitle = models.CharField(max_length=255)
    ordesc = models.TextField()
    orimg = models.ImageField(upload_to = 'ordered_products')
    orqnty =  models.IntegerField()
    oraddress = models.CharField(max_length=255)
    orpin = models.IntegerField()
    ordist =  models.CharField(max_length=255)
    orcntry =  models.CharField(max_length=255)
    orprice =  models.IntegerField()

    def __str__(self):
        return self.ortitle

# class Electronics_ProductDetail(models.Model):
#     ortitle1 = models.CharField(max_length=255)
#     ordesc1 = models.TextField()
#     orimg1 = models.ImageField(upload_to = 'ordered_products')
#     orqnty1 =  models.IntegerField()
#     oraddress1 = models.CharField(max_length=255)
#     orpin1 = models.IntegerField()
#     ordist1 =  models.CharField(max_length=255)
#     orcntry1 =  models.CharField(max_length=255)
#     def __str__(self):
#         return self.ortitle1

# class Utencils_ProductDetail(models.Model):
#     ortitle2 = models.CharField(max_length=255)
#     ordesc2 = models.TextField()
#     orimg2 = models.ImageField(upload_to = 'ordered_products')
#     orqnty2 =  models.IntegerField()
#     oraddress2 = models.CharField(max_length=255)
#     orpin2 = models.IntegerField()
#     ordist2 =  models.CharField(max_length=255)
#     orcntry2 =  models.CharField(max_length=255)

#     def __str__(self):
#         return self.ortitle2