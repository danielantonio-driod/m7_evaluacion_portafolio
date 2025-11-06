from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Uno a muchos
    productos = models.ManyToManyField(Producto)  # Muchos a muchos
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  # Uno a uno
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"
