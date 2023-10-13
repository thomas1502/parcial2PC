from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Venta {self.id}"

class Detalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Detalle de {self.producto.nombre} en {self.venta}"

#Clase parcial1    
class Solicitud(models.Model):
    tipo_solicitud = models.CharField(max_length=100)
    codigo_solicitud = models.CharField(max_length=50)

    def __str__(self):
        return f"Solicitud {self.id}"

#Clase parcial2     
class Ordenes(models.Model):
    id = models.ImageField
    nombreCliente = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=5, decimal_places = 2)

    def __str__(self):
        return f"Ordenes {self.id}"


#tablas de ejercicio

class Proveedor(models.Model):
    Nombre_proveedor = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre_proveedor

class Cliente(models.Model):
    Nombres = models.CharField(max_length=100)
    DPI = models.CharField(max_length=20, unique=True)
    Telefono = models.CharField(max_length=15)
    Edad = models.PositiveIntegerField()

    def __str__(self):
        return self.Nombres

class Banco(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre