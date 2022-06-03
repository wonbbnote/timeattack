from django.urls import path
from . import views

urlpatterns = [
    path('main', views.product_view, name='main'),
]