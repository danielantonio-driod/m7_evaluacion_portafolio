# Modelos con Relaciones en Django

## Descripción
Este proyecto muestra cómo implementar la capa de modelo de acceso a datos utilizando entidades con relaciones uno a uno, uno a muchos y muchos a muchos en Django.

### Objetivos
- Utilizar los tipos de relaciones proporcionados por Django (ForeignKey, OneToOneField, ManyToManyField).
- Modelar entidades interconectadas para dar solución a una problemática.

---

## Ejemplo de Modelos con Relaciones

```python
# models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Uno a muchos
    productos = models.ManyToManyField(Producto)  # Muchos a muchos
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  # Uno a uno
    direccion = models.CharField(max_length=200)
```

## Explicación
- `Pedido` tiene una relación de uno a muchos con `Cliente` y de muchos a muchos con `Producto`.
- `PerfilCliente` tiene una relación uno a uno con `Cliente`.

---

