from django.urls import path, reverse_lazy
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.HomeView.as_view(), name='books_home'),
    path('book', views.BookListView.as_view(), name='all_books'),
    path('book/<int:pk>', views.BookDetailedView.as_view(), name='book_detail'),

    path('book/new', views.CreateBookView.as_view(success_url=reverse_lazy('books:all_books')), name='book_create'),
    path('book/<int:pk>/edit', views.EditBookView.as_view(success_url=reverse_lazy('books:all_books')), name='book_edit'),
    path('book/<int:pk>/delete', views.DeleteBookView.as_view(success_url=reverse_lazy('books:all_books')), name='book_delete'),

    path('author', views.AuthorListView.as_view(), name='all_authors'),
    path('author/new', views.CreateAuthorView.as_view(success_url=reverse_lazy('books:all_authors')), name='author_create'),

]
