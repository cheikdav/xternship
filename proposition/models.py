# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proposition(models.Model):    
    
    titre = models.CharField(max_length = 400)
    description = models.TextField()
    
    proposeur = models.CharField(max_length = 500)
    contact_mail = models.EmailField(default = '')
    
    
    date_publication = models.DateField('Date de publication de l\'annonce')
    date_fin = models.DateField('Date de fin de visibilité') #Mettre une valeur par défaut pour ne pas encombrer. Peut etre transformer en temps d'affichage
    validee = models.BooleanField()
    
    type_prop = models.CharField(max_length = 20, choices = ((0,'PSC'),(1, 'Stage 2A'),(2,'Stage 3A')))
    lieu = models.CharField(max_length = 300, blank = True)
    periode = models.CharField(max_length = 400, blank = True)
    
    def __str__(self):
	return '['+self.type_prop+'] '+self.titre
    
    




    