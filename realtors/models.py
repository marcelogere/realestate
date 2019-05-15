from django.db import models
from datetime import datetime

class Realtor(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(max_length=200, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nombre