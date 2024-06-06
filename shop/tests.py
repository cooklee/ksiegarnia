import pytest
from django.test import TestCase, Client
from django.urls import reverse

from shop.forms import AddCommentForm, AddBookForm
from shop.models import Author, Book, Publisher, Magazine, CartBook, Order


# Create your tests here.
def test_base_view():
    url = reverse('base')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db
def test_author_list(authors):
    url = reverse('author_list')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['authors'].count() == len(authors)
    for a in authors:
        assert a in response.context['authors']


@pytest.mark.django_db
def test_book_list(books):
    url = reverse('book_list')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(books)
    for a in books:
        assert a in response.context['object_list']



@pytest.mark.django_db
def test_costam(book):
    url = reverse('detail_book', args=(book.pk,))
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    book_context = response.context['object'] ## book_context = response.context['book']
    assert book_context == book
    form = response.context['form']
    assert isinstance(form, AddCommentForm)


def test_add_author_get():
    url = reverse('add_author')
    client = Client()
    response = client.get(url)
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url == f'{login_url}?next={url}'

@pytest.mark.django_db
def test_add_author_get_login(user):
    url = reverse('add_author')
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
@pytest.mark.django_db
def test_add_author_post(user):
    url = reverse('add_author')
    client = Client()
    client.force_login(user)
    dane = {
        'first_name': 'Jan',
        'last_name': 'Kowalski'
    }
    response = client.post(url, dane)
    assert response.status_code == 200
    assert Author.objects.get(first_name='Jan', last_name='Kowalski')


@pytest.mark.django_db
def test_add_book_get():
    url = reverse('add_book')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddBookForm)

@pytest.mark.django_db
def test_add_book_post(author):
    url = reverse('add_book')
    client = Client()
    data = {
        'title': 'Test',
        'author': author.id,
        'published_date': '2021-01-01',
        'isbn': '1234567890123',
        'price': 10.0
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Book.objects.get(title="Test")


@pytest.mark.django_db
def test_add_book_post(author):
    url = reverse('add_book')
    client = Client()
    data = {
        'title': 'test',
        'author': author.id,
        'published_date': '2021-01-01',
        'isbn': '1234567890123',
        'price': 10.0
    }
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_magazine_post(publisher):
    url = reverse('add_magazine')
    client = Client()
    data = {
        'title': 'test',
        'publisher':publisher.pk ,
        'published_date': '2021-01-01',
        'isbn': '1234567890123',
        'no_pages': 14.0,
        'period':1
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Magazine.objects.get(title='test')


@pytest.mark.django_db
def test_add_book_to_cart(book, user):
    url = reverse('add_book_to_cart', args=(book.pk,))
    client = Client()
    client.force_login(user)
    response = client.get(url)
    redirect_url = reverse('book_list')
    assert response.status_code == 302
    assert response.url == redirect_url
    assert CartBook.objects.get(book=book,quantity=1)

@pytest.mark.django_db
def test_create_order(cart):
    url = reverse('create_order')
    client = Client()
    client.force_login(cart.user)
    book_count = cart.books.count()
    response = client.post(url)
    assert response.status_code == 302
    redirect_url = reverse('cart')
    assert response.url == redirect_url
    o = Order.objects.get(user=cart.user)
    assert o.books.count() == book_count