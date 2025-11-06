# Aplicaciones Preinstaladas en Django

## Descripción
Este proyecto reconoce y explica la utilidad de las aplicaciones preinstaladas con el motor Django como apoyo al desarrollo.

### Objetivos
- Identificar y explicar el propósito de aplicaciones preinstaladas en Django.
- Configurar y personalizar el panel de administración para gestionar modelos.

---

## Ejemplo de Proyecto: Personalización del Admin

### Estructura del Proyecto
- carpeta: ejemplo_admin
  - manage.py
  - ejemplo_admin/
    - settings.py
    - ...
  - productos/
    - models.py
    - admin.py

### Ejemplo de Configuración de Admin
```python
# productos/admin.py
from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')

admin.site.register(Producto, ProductoAdmin)
```

## Explicación
- `django.contrib.admin`: Permite gestionar los modelos desde una interfaz web.
- `django.contrib.auth`: Proporciona autenticación y gestión de usuarios.
- `django.contrib.sessions`: Maneja sesiones de usuario.
- El archivo `admin.py` permite personalizar la visualización y gestión de modelos en el panel de administración.

---

