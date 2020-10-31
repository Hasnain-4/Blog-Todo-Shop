from django.db import models
from datetime import datetime , date

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=2000)
    desc = models.TextField()
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
    