from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),
    path('bags/', views.bags, name='bags'),
    path('crossbody/', views.crossbody, name='crossbody'),
    path('backpack/', views.backpack, name='backpack'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderplaced/', views.orderplaced, name='orderplaced'),

]
