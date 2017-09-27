# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Proposition
from django.http import HttpResponse
from django.template import loader
from .forms import Type_Recherche, Categorie_Recherche

# Create your views here.
def index(request):
    
    if request.method == "POST":
	type_rech = Type_Recherche(request.POST)
	cat_rech = Categorie_Recherche(request.POST)
    else:
	type_rech = Type_Recherche()
	cat_rech = Categorie_Recherche()
    
    latest_propositions = Proposition.objects.order_by('-date_publication')[:5]
    
    return render(request, 'proposition/index.html', {'latest_proposition': latest_propositions, 'type_rech' : type_rech, 'cat_rech' : cat_rech})

def detail_prop(request, prop_id):
    prop = get_object_or_404(Proposition,pk= prop_id)
    return render(request, 'proposition/detail_prop.html', {'prop' : prop})

    