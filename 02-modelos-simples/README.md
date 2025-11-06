# Modelos Simples en Django

## Descripción
Este proyecto muestra cómo implementar la capa de modelo de acceso a datos utilizando entidades no relacionadas en Django.

### Objetivos
- Crear modelos simples en Django sin relaciones entre ellos.
- Permitir la creación de tablas independientes en la base de datos.

---

## Ejemplo de Modelo Simple

```python
# models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
```

## Explicación
- El modelo `Producto` tiene campos básicos: nombre, precio y cantidad.
- No tiene relaciones con otras entidades, por lo que la tabla en la base de datos es independiente.

---

