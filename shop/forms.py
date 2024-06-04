from django import forms
import string
from shop.models import Author, Magazine


def check_if_upper(value):
    if value[0] in string.ascii_lowercase:
        raise forms.ValidationError('Pierwsza litera musi być wielka')

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=100, validators=[check_if_upper], widget=forms.TextInput(attrs={'placeholder': 'Tytuł', 'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    published_date = forms.DateField()
    isbn = forms.CharField(max_length=13)


class AddMagazineForm(forms.ModelForm):

    class Meta:
        model = Magazine
        fields = "__all__" # ['title', 'publisher']
        #exclude = ['title']

    def clean(self):
        cleaned_data = super().clean()
        period = cleaned_data.get('period') #cleaned_data['period']
        no_pages = cleaned_data.get('no_pages')
        if period == 1 and no_pages < period*10:
            raise forms.ValidationError('Nie może być mniej niż 10 stron dla dziennika')
        elif period == 2 and no_pages < 20:
            raise forms.ValidationError('Nie może być mniej niż 20 stron dla tygodnika')
        elif period == 3 and no_pages < 30:
            raise forms.ValidationError('Nie może być mniej niż 30 stron dla miesięcznika')
        elif period == 4 and no_pages < 40:
            raise forms.ValidationError('Nie może być mniej niż 40 stron dla rocznika')
        return cleaned_data



