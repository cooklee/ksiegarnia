import pytest

from shop.models import Author, Book


@pytest.fixture
def authors():
    lst = []
    for i in range(5):
        lst.append(Author.objects.create(first_name=i, last_name=i))
    return lst


@pytest.fixture
def books(authors):
    lst = []
    for i, author in enumerate(authors):
        lst.append(Book.objects.create(title=i, author=author, published_date='2023-02-02', isbn=i, price=i))
    return lst


@pytest.fixture
def author():
    return Author.objects.create(first_name='ala', last_name='bala')
@pytest.fixture
def book(author):
    return Book.objects.create(title='ala', author=author, published_date='2023-02-02', isbn='1234567890123', price=10.0)