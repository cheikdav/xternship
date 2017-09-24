# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Proposition
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    
    latest_propositions = Proposition.objects.order_by('-date_publication')[:5]
    context = {'latest_proposition': latest_propositions}
    return render(request, 'proposition/index.html', context)

def detail_prop(request, prop_id):
    prop = get_object_or_404(Proposition,pk= prop_id)
    return render(request, 'proposition/detail_prop.html', {'prop' : prop})

