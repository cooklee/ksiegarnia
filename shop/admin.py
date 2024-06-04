from django.contrib import admin

from shop.models import Publisher, Author, Book, Magazine

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Magazine)
