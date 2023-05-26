from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()
    nivel = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
