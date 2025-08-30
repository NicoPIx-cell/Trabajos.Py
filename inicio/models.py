from django.db import models

class Computadora(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="imagenes_computadoras", null=True)
    precio = models.IntegerField(help_text="Precio en dólares")
    
    def __str__(self):
        return f"{self.modelo} {self.marca}"