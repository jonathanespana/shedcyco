from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

CATEGORIES = (
  ('C', 'Clothing'),
  ('A', 'Accessories'),
  ('G', 'Gear')
)

class Item(models.Model):
  name = models.CharField(max_length=150)
  main_image = models.URLField(max_length=200)
  price = models.FloatField(max_length=10)
  logos = models.CharField(max_length=100)
  method = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  origin = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  featured = models.BooleanField(default=false)
  category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
