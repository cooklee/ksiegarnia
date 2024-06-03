from django import forms

from shop.models import Author


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    published_date = forms.DateField()
    isbn = forms.CharField(max_length=13)