from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return redirect('lista_productos')
    return render(request, 'productos/formulario.html')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.cantidad = request.POST['cantidad']
        producto.save()
        return redirect('lista_productos')
    return render(request, 'productos/formulario.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')
