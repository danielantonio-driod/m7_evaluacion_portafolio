# Migraciones en Django

## Descripción
Este proyecto explica cómo utilizar migraciones para la propagación de cambios al esquema de base de datos en Django.

### Objetivos
- Ejecutar migraciones para crear y modificar tablas en la base de datos.
- Propagar cambios realizados en los modelos de datos.

---

## Ejemplo de Uso de Migraciones

1. Crear migraciones:
   ```bash
   python manage.py makemigrations
   ```
2. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
3. Ejemplo de agregar un campo a un modelo:
   ```python
   # models.py
   class Producto(models.Model):
       nombre = models.CharField(max_length=100)
       precio = models.DecimalField(max_digits=10, decimal_places=2)
       cantidad = models.IntegerField()
       descripcion = models.TextField(null=True, blank=True)  # Nuevo campo
   ```
   Luego, ejecutar los comandos anteriores para propagar el cambio.

## Explicación
- Las migraciones permiten mantener sincronizado el esquema de la base de datos con los modelos definidos en Django.
- Cada vez que se modifica un modelo, se debe crear y aplicar una migración.

---

