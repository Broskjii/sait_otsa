from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auto-repair/', views.auto_repair, name='auto_repair'),
    path('cargo-transport/', views.cargo_transport, name='cargo_transport'),
]