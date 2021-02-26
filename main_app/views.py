from django.shortcuts import render

from .models import Item

# Create your views here.

# === Home ===
def home(request):
  ft_items = Item.objects.filter(featured=True)
  context = { 'ft_items': ft_items }
  return render(request, 'home.html', context)

# === Shop all products ===
def shop_all(request):
  items = Item.objects.all()
  context = { 'items': items }
  return render(request, 'shop.html', context)

# === Shop apparel
def shop_apparel(request):
  items = Item.objects.filter(category="C")
  context = { 'items': items }
  return render(request, 'apparel.html', context)

# === Shop product ===
def item_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  context = { 'item': item }
  return render(request, 'item.html', context)
  
