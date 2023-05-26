from django.db import models
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField()
    professor = models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
