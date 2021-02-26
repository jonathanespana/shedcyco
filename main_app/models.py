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
  designer = models.CharField(max_length=50)
  main_image = models.URLField(max_length=200)
  price = models.DecimalField(decimal_places=2, max_digits=6)
  logos = models.CharField(max_length=100)
  method = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  material = models.CharField(max_length=100)
  origin = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
  featured = models.BooleanField(default=False)
  soldout = models.BooleanField(default=False)