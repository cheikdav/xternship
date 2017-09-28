from django import forms
from models import Categorie

class Type_Recherche(forms.Form):
    choix = ((0,'PSC'), (1, '1A'),(2,'2A'))
    print(choix)
    type_stage = forms.MultipleChoiceField(label = '', choices = choix , widget=forms.CheckboxSelectMultiple(), initial = [c[0] for c in choix] )
    cat_voulues = forms.ModelMultipleChoiceField(label = 'Categories', queryset = Categorie.objects.all(), widget=forms.CheckboxSelectMultiple(), initial = Categorie.objects.all()) 

    def clean_my_field(self):
        if len(self.cleaned_data['type_stage']) == 0:
            raise forms.ValidationError('Choisir au moins un type de proposition')
	if len(self.cleaned_data['cat_voulues']) == 0:
            raise forms.ValidationError('Choisir au moins une categorie')
        return super(Type_Recherche, self).clean()
    

	