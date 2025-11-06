from django.shortcuts import render
from .models import Pedido

def pedidos_por_cliente(request):
    pedidos = Pedido.objects.filter(cliente__nombre="Juan", fecha__range=["2025-01-01", "2025-12-31"])
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})
