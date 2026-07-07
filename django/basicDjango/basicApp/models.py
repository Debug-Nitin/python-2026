from django.db import models
from django.utils import timezone

# Create your models here.
class appvariety(models.Model):
    APP_TYPE_CHOICE = [
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Grain', 'Grain'),
        ('Legume', 'Legume'),
        ('Nut', 'Nut'),
        ('Herb', 'Herb'),
        ('Spice', 'Spice')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='basics/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=10 ,choices=APP_TYPE_CHOICE)
    description = models.TextField(default='')

def __str__(self):
    return self.name
