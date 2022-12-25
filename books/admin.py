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


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'book_title',
                    'num_pages', 'book_language', 'publication_date']
    search_fields = ['publisher__publisher_name__istartswith',
                     'book_title__istartswith']
    list_filter = ['book_language']
    list_per_page = 10
    list_editable = ['num_pages', 'book_language']
    fields = ['book_author', 'publisher', 'book_title',
              'description', 'num_pages', 'book_language', 'publication_date']
    autocomplete_fields = ['book_author', 'publisher', 'book_language']

    class Meta:
        ordering = ['-publication_date']
