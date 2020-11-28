from django.db import models

# Create your models here.


class Medicina(models.Model):

    TIPO_M = [
        ('G', 'Generico'),
        ('C', 'Comercial'),
    ]

    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()
    tipo_medicamento = models.CharField(max_length=12, choices=TIPO_M)
    
    def __str__(self) -> str:
        return self.nombre + '  ' + self.TIPO_M + ' - ' + str(self.codigo)

