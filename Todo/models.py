from django.db import models
from datetime import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



