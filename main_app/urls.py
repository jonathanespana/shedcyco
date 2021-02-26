from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('shop/', views.shop_all, name='shop_all'),
  path('shop/apparel/', views.shop_apparel, name='shop_apparel'),
  path('shop/<int:item_id>/', views.item_detail, name='item_detail'),
]