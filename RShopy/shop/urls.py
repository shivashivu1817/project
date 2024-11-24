from django.contrib import admin
from django.urls import path
from . import views
from .views import fibonacci_view

urlpatterns = [

    path('h', views.home, name='home'),

    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('product-details', views.product_details, name='product-details'),
    path('checkout', views.checkout, name='checkout'),
    path('p',views.SignupPage,name='signup'),
    path('login/',views.login_view,name='login'),
    path('home/',views.HomePage,name='hom'),
    path('logout/',views.LogoutPage,name='logout'),
   
    path('fibonacci', fibonacci_view, name='fibonacci'),
    path('ind', views.index, name='index'),
    path('prime', views.prime_view, name='prime_view'),


]

