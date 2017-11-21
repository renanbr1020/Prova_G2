from django.db import models

# Create your models here.

class Eleicao (models.Model):
     local = models.CharField(max_length=20)
     dataInicio = models.DateTimeField(blank=False, null=False)
     dataFim = models.DateTimeField(blank=False, null=False)



class Token (models.Model):
    codigo = models.CharField(max_length=5,blank=False,null=False,unique=True)
    def __str__ (self):
        return self.codigo

class Candidato (models.Model):
    nome = models.CharField(max_length=40)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    idade = models.CharField(max_length=3)
    def __str__ (self):
        return self.nome

class Vaga (models.Model):
    cargo = models.CharField(max_length=40)
    candidato = models.ManyToManyField (Candidato)
    def __str__(self):
        return self.cargo

class Eleitor (models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=14)
    token = models.ForeignKey (Token)
    def __str__ (self):
        return self.nome

class Votacao (models.Model):
    eleitor = models.ForeignKey (Eleitor)
    candidato = models.ForeignKey (Candidato,blank=True,null=True)
    votoBranco = models.BooleanField("Voto em branco",default=False)
    dataHora = models.DateTimeField(blank=False, null=False)
    def __str__ (self):
        return "Eleitor: "+self.eleitor.nome

