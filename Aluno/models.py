from django.db import models

class Aluno(models.Model):
    
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    matricula = models.IntegerField()
    cpf = models.IntegerField()
    
    def __str__(self):
        return self.nome
