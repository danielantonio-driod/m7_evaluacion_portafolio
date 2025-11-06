# Integración de Django con Bases de Datos

## Descripción
En este proyecto se describen las características fundamentales de la integración del framework Django con bases de datos.

### Objetivos
- Explicar cómo Django se integra con diferentes sistemas de bases de datos (SQLite, PostgreSQL, MySQL).
- Describir cómo Django maneja las conexiones y operaciones con la base de datos a través de su ORM.
- Ejemplo de configuración de `settings.py` para conectar Django con una base de datos.

---

## Ejemplo de configuración en `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Cambia a 'sqlite3', 'mysql', etc. según el motor
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Explicación
- Django utiliza el archivo `settings.py` para definir la configuración de la base de datos.
- El ORM de Django permite interactuar con la base de datos usando modelos Python, sin escribir SQL directamente.
- Django soporta múltiples motores de bases de datos y gestiona las conexiones automáticamente.

---

