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
