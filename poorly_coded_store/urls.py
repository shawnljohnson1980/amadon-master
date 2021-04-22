from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('check_out',views.check_out),
    path('product_create',views.product_create),
    path('create_product',views.create_product),
]
