from django.db import models
from django.urls import reverse

# Create your models here.

class Bear(models.Model):
    name=models.CharField(max_length=124)
    taste=models.CharField(max_length=124)
    color=models.CharField(max_length=124)
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.id})


