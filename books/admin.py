from django.contrib import admin
from .models import Author, Publisher, Book, BookLanguage

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookLanguage)
admin.site.register(Book)
