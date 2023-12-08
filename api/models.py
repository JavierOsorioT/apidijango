
# Create your models here.
from django.db import models

class Respuestaschatbot(models.Model):
    
    marca_temporal = models.DateTimeField()
    nombre_completo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=2)
    pregunta2 = models.TextField()
    pregunta3 = models.CharField(max_length=10)
    pregunta4 = models.TextField()
    pregunta5 = models.TextField()
    pregunta6 = models.CharField(max_length=20)
    pregunta7 = models.CharField(max_length=10)

    def _str_(self):
        return str(self.nombre_completo)

# Create your models here.
class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    password_repeat = models.CharField(max_length=50)
    email = models.EmailField()
    
