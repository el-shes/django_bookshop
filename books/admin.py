from django.contrib import admin
from .models import Author, Publisher, Book, BookLanguage


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_first_name', 'author_first_name']
    search_fields = ['author_first_name__istartswith',
                     'author_last_name__istartswith']


admin.site.register(Publisher)
admin.site.register(BookLanguage)
admin.site.register(Book)
