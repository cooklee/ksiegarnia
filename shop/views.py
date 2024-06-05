from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from shop.forms import AddBookForm, AddMagazineForm, AddCommentForm
from shop.models import Author, Book, Publisher, Cart, CartBook, Order, OrderBook


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
            price = form.cleaned_data['price']
            Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn, price = price)
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

class ShowCardView(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, "shop/cart.html", {"cart": cart})


class CreateOrderView(LoginRequiredMixin, View):
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        if created or not cart.cartbook_set.all():
            return redirect("cart")
        order = Order.objects.create(user=request.user)
        for cart_book in cart.cartbook_set.all():
            OrderBook.objects.create(book=cart_book.book,
                                     order=order,
                                     quantity=cart_book.quantity)
        # for cart_book in cart.cartbook_set.all():
        #     OrderBook.objects.create(book=cart_book.book, order=order, quantity=cart_book.quantity)
        cart.cartbook_set.all().delete()
        return redirect("cart")

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "shop/order_list.html"
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class DetailOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "shop/order_detail.html"

class DetailBookView(DetailView):
    model = Book
    template_name = "shop/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        return context
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, book_pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(pk=book_pk)
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect("detail_book", book_pk)
        return render(request, "shop/book_detail.html", {"form": form})
