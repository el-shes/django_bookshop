from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Author
from django.db.models import Q


class HomeView(TemplateView):
    model = Book
    template_name = "books/home.html"


class BookListView(View):
    model = Book
    template_name = "books/books_list.html"

    def get(self, request, authors=None):
        """
        Search page request. If not all books are displayed.
        :param request:
        :param authors: gets updated to display author_first_name and author_last_name
        :return: rendered page
        """
        query = request.GET.get("search", False)
        if query:
            search_result = Book.objects.filter(book_author__book__book_title__icontains=query).select_related()
        else:
            search_result = Book.objects.all()

        for book in search_result:
            authors = []
            for author in book.book_author.all():
                authors.append("{0} {1}".format(author.author_first_name, author.author_last_name))
            book.book_author_updated = authors
        book_list = search_result
        ctx = {'book_list': book_list}
        return render(request, self.template_name, ctx)


class BookDetailedView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

#     def get_queryset(self):
#         query = self.request.GET.get('search_box', False)
#         if query:
#             object_list = Book.objects.filter(book_author__book__book_title__icontains=query)
#             return object_list
#         # object_list = Book.objects.filter(Q(book_title__icontains=query))
#         # return object_list
