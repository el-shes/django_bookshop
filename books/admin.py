from django.contrib import admin
from .models import Author, Publisher, Book, BookLanguage


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_first_name', 'author_first_name']
    search_fields = ['author_first_name__istartswith',
                     'author_last_name__istartswith']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher_name']
    search_fields = ['publisher_name__istartswith']


@admin.register(BookLanguage)
class BookLanguageAdmin(admin.ModelAdmin):
    list_display = ['language_name']
    search_fields = ['language_name__istartswith']
