from django.shortcuts import render

# Create your views here.

# === Home ===
def home(request):
  return render(request, 'home.html')

def shop_all(request):
  return render(request, 'shop.html')
