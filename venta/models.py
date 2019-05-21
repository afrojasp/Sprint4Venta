from django.db import models

class Venta(models.Model):
    idVenta = models.IntegerField(null=False, default=None)
    producto = models.IntegerField(null=False, default=None)
    cantidad = models.IntegerField(null=False, default=None)
    total = models.PositiveIntegerField()

    def __str__(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.idVenta, self.producto, self.cantidad, self.total)

# Create your models here.
