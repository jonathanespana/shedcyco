from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('shop/allproducts/', views.shop_all, name='shop_all'),
  path('shop/product/', views.shop_product, name='shop_product')
]