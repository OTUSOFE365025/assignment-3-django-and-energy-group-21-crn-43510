from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan, name='scan'),
    path('load/', views.load_products, name='load_products'),
]
