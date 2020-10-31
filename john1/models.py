from django.db import models
from datetime import datetime , date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics', default = None,null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
    