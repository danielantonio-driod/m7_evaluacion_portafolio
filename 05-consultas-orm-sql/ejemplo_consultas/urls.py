from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedidos_por_cliente, name='pedidos_por_cliente'),
]
