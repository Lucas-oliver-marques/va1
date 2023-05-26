from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    sexo = models.CharField(max_length=1)
    experiencia = models.IntegerField()
    
    def __str__(self):
        return self.nome
