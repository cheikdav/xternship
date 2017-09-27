# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Proposition
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

from .forms import PropForm

# Create your views here.

@login_required(login_url = 'cas_ng_login')
def index(request):
    
    latest_propositions = Proposition.objects.order_by('-date_publication')[:5]
    context = {'latest_proposition': latest_propositions}
    return render(request, 'proposition/index.html', context)

@login_required(login_url = 'cas_ng_login')
def detail_prop(request, prop_id):
    prop = get_object_or_404(Proposition,pk= prop_id)
    return render(request, 'proposition/detail_prop.html', {'prop' : prop})

@login_required(login_url = 'cas_ng_login')
def nouvelle_prop(request):
    if request.method == 'POST':
        #il faudra envoyer ici à l'admin pour validation
        form = PropForm(request.POST)
    else:
        form = PropForm()
    return render(request, 'proposition/nouvelle_prop.html',{'form': form})
