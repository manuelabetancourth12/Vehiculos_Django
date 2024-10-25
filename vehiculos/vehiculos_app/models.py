from django.db import models


# Create your models here.

class vehiculo(models.Model):

    COLOR=(
        ('1','ROJO'),
        ('2','AZUL'),
        ('3','VERDE'),
        ('4','MORADO'),
        ('5','ROSADO'),
        ('6','LILA'),
        ('7','AMARILLO'),
    )

    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color=vehiculo=models.CharField('color', max_length=1, choices=COLOR)
    modelo=models.IntegerField()

    def __str__(self):
        return self.placa