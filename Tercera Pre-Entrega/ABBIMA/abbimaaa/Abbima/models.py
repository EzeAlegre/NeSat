from django.db import models

# Create your models here.
class Curso(models.Model):
    comision=models.IntegerField()  
    nombre=models.CharField(max_length=20 )
    def __str__(self):
        return f"{self.nombre} - {self.comision}"    

class Estudiante(models.Model):
    apellido=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 


