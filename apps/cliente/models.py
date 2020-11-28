from django.db import models

# Create your models here.

class dato(models.Model):
   
    GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    IDENTIFICACION = [
        ('RE', 'Registro Civil'),
        ('TI', 'Tarjeta Identidad'),
        ('CE', 'Cedula'),
    ]
    
   

    codigo = models.CharField(max_length=10,primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    tipo_identificacion = models.CharField(max_length=12, choices=IDENTIFICACION)
    identificacion = models.IntegerField(null=True)
    sexo = models.CharField(max_length=10, choices=GENERO)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    #persona = models.ForeignKey(persona, null = True, blank= True, on_delete = models.CASCADE)
    #antecedentes_medico = models.ManyToManyField(antecedentes_medico)

    def __str__(self) -> str:
        return self.nombres + '  ' + self.apellidos + ' - ' + str(self.codigo)
