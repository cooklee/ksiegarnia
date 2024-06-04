from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from shop.forms import AddBookForm, AddMagazineForm
from shop.models import Author, Book, Publisher, Cart, CartBook


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

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            published_date = form.cleaned_data['published_date']
            isbn = form.cleaned_data['isbn']
            Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
            return redirect('add_book')
        return render(request, "shop/form.html", {"form": form})
class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, "shop/author_list.html", {"authors": authors})


class AddMagazineView(View):

    def get(self, request):
        form = AddMagazineForm()
        return render(request, "shop/form.html", {"form": form})

    def post(self, request):
        form = AddMagazineForm(request.POST)
        if form.is_valid():
            magazine = form.save()
            return redirect('add_magazine')
        return render(request, "shop/form.html", {"form": form})


class AddPublisherView(CreateView):
    model = Publisher
    fields = "__all__"
    template_name = "shop/form.html"
    success_url = reverse_lazy("add_publisher")

class PublisherListView(ListView):
    model = Publisher
    template_name = "shop/publisher_list.html"


class UpdatePublisherView(UpdateView):
    model = Publisher
    fields = "__all__"
    template_name = "shop/form.html"

    def get_success_url(self):
        return reverse("update_publisher", args=(self.get_object().pk,))

class DeletePublisherView(DeleteView):
    model = Publisher
    template_name = "shop/delete_form.html"
    success_url = reverse_lazy("list_publisher")

class BookListView(ListView):
    model = Book
    template_name = "shop/book_list.html"


class AddBookToCartView(View):

    def get(self, request, book_pk):
        book = Book.objects.get(pk=book_pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        try:
            cartItem = CartBook.objects.get(book=book, cart=cart)
            cartItem.quantity += 1
            cartItem.save()
        except CartBook.DoesNotExist:
            cart.books.add(book)
        return redirect("book_list")