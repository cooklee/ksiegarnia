from django import forms

from przepisy.models import SkladnikWPrzepisie


class DodajSkladnikForm(forms.ModelForm):


    class Meta:
        model = SkladnikWPrzepisie
        fields = ['skladnik', 'ilosc', 'jednostka']
