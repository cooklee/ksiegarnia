from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.FloatField(default=10.0)

    def __str__(self):
        return f"{self.title} {self.author} {self.published_date} {self.isbn}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.address}"

class Magazine(models.Model):
    PERIODS = (
        (1, 'Daily'),  # 10
        (2, 'Weekly'),  # 30
        (3, 'Monthly'),  # 50
        (4, 'Yearly')  # 100
    )
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    no_pages = models.IntegerField(default=101)
    period = models.IntegerField(choices=PERIODS, default=1)
    def __str__(self):
        return f"{self.title}"

class CartBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total(self):
        return self.quantity * self.book.price
class Cart(models.Model):
    books = models.ManyToManyField(Book, through='CartBook')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total(self):
        """
        prostolinijny przykład natomiast to nie jest optymalne rozwiązanie
        optypamlne rozwiązanie to zrobienie zapytania do bazy danych przez funkcje agregujące
        """

        total = 0
        for cb in self.cartbook_set.all():
            total += cb.total()
        return total


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total(self):
        return self.quantity * self.book.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='OrderBook')
    date = models.DateField(auto_now_add=True)

    def total(self):
        total = 0
        for ob in self.orderbook_set.all():
            total += ob.total()
        return total