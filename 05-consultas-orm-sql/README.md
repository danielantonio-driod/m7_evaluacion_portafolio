# Consultas ORM y SQL en Django

## Descripción
Este proyecto muestra cómo realizar consultas de filtrado de datos y consultas personalizadas utilizando el ORM y sentencias SQL en Django.

### Objetivos
- Utilizar el ORM de Django para realizar consultas de filtrado de datos.
- Crear consultas personalizadas utilizando métodos como filter(), exclude(), get(), annotate().
- Realizar consultas SQL directas cuando sea necesario.

---

## Ejemplo de Proyecto: Consultas de Pedidos

### Estructura del Proyecto
- carpeta: ejemplo_consultas
  - manage.py
  - ejemplo_consultas/
    - settings.py
    - ...
  - pedidos/
    - models.py
    - views.py
    - ...

### Ejemplo de Consulta ORM
```python
# views.py
from pedidos.models import Pedido
from django.utils import timezone

# Recuperar todos los pedidos de un cliente en un rango de fechas
pedidos = Pedido.objects.filter(
    cliente__nombre="Juan",
    fecha__range=["2025-01-01", "2025-12-31"]
)
```

### Ejemplo de Consulta SQL
```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM pedidos_pedido WHERE fecha BETWEEN %s AND %s", ["2025-01-01", "2025-12-31"])
    results = cursor.fetchall()
```

## Explicación
- El ORM permite realizar consultas complejas de manera sencilla y segura.
- También es posible ejecutar sentencias SQL directamente si se requiere mayor control.

---

