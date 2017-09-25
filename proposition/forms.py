from django import forms

from proposition.choices import *

class PropForm(forms.Form):
    titre = forms.CharField(label = 'Titre', max_length = 400)
    description = forms.CharField(label = 'Description', widget=forms.Textarea)

    
    proposeur = forms.CharField(label = 'Proposé par', max_length = 500)
    contact_mail = forms.EmailField(label ='mail')

    date_publication = forms.DateField(label = 'date de publication',
                                       input_formats='%d/%m/%Y')
    date_fin = forms.DateField(label = 'Date de fin de visibilité',
                               input_formats='%d/%m/%Y')

    type_prop = forms.MultipleChoiceField(label = 'Quel est le type de votre proposition?',
                                          choices = TYPE_CHOICES,
                                          widget = forms.CheckboxSelectMultiple)
    

    #Reste lieu et période            
