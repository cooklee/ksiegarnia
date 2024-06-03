from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from shop.forms import AddBookForm
from shop.models import Author


# Create your views here.
class AddAuthorView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "shop/add_author.html")

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
        return render(request, "shop/add_author.html", {"success": f"Author {first_name} {last_name} added successfully"})

class AddBookView(View):

    def get(self, request):
        form = AddBookForm()
        return render(request, "shop/form.html", {"form": form})
class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, "shop/author_list.html", {"authors": authors})