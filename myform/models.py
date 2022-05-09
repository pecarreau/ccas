from pyexpat import model
from django.db import models

# Create your models here.
from django.contrib import admin
from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom


class Aide(models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Droit(models.Model):
    aide = models.ForeignKey(Aide, on_delete=models.CASCADE) 
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.aide, self.personne)
