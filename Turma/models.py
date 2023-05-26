from django.db import models
class Turma(models.Model):
    codigo = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
