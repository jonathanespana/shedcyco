from django.shortcuts import render

# Create your views here.

# === Home ===
def home(request):
  return render(request, 'home.html')

# === Shop all products ===
def shop_all(request):
  return render(request, 'shop.html')

# === Shop product ===
def shop_product(request):
  return render(request, 'product.html')
  
