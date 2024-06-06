import pytest
from django.test import TestCase, Client
from django.urls import reverse

from shop.forms import AddCommentForm
from shop.models import Author


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
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_author_post():
    url = reverse('add_author')
    client = Client()
    dane = {
        'first_name': 'Jan',
        'last_name': 'Kowalski'
    }
    response = client.post(url, dane)
    assert response.status_code == 200
    assert Author.objects.get(first_name='Jan', last_name='Kowalski')