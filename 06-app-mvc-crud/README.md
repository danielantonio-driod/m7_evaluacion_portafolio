# Aplicación MVC CRUD en Django

## Descripción
Este proyecto implementa una aplicación web MVC que realiza operaciones CRUD en la base de datos utilizando los componentes del framework Django.

### Objetivos
- Crear una aplicación Django que implemente las operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
- Utilizar vistas, modelos y plantillas para gestionar los datos.

---

## Ejemplo de Proyecto: Gestión de Productos

### Estructura del Proyecto
- carpeta: gestion_productos
  - manage.py
  - gestion_productos/
    - settings.py
    - ...
  - productos/
    - models.py
    - views.py
    - templates/
      - productos/
        - lista.html
        - formulario.html
    - urls.py

### Ejemplo de Modelo
```python
# productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
```

### Ejemplo de Vista CRUD
```python
# productos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Listar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return redirect('lista_productos')
    return render(request, 'productos/formulario.html')

# Editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.cantidad = request.POST['cantidad']
        producto.save()
        return redirect('lista_productos')
    return render(request, 'productos/formulario.html', {'producto': producto})

# Eliminar producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')
```

## Explicación
- Se implementan las operaciones CRUD usando vistas y modelos de Django.
- Las plantillas permiten mostrar y editar los datos de forma sencilla.

---

