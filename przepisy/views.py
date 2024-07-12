from django.shortcuts import render, redirect
from django.views import View

from przepisy.forms import DodajSkladnikForm
from przepisy.models import Przepis


class DodajSkladnikDoPrzepisu(View):

    def get(self, request, pk):
        przepis = Przepis.objects.get(pk=pk)
        form = DodajSkladnikForm()
        return render(request, 'shop/form.html', {'form':form, 'przepis':przepis })

    def post(self, request, pk):
        przepis = Przepis.objects.get(pk=pk)
        form = DodajSkladnikForm(request.POST)
        if form.is_valid():
            swp = form.save(commit=False)
            swp.przepis = przepis
            swp.save()
            return redirect('dswp', pk)


# Create your views here.
