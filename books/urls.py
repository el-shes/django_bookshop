from django.urls import path
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.HomeView.as_view(), name='books_home'),
    path('book', views.BookListView.as_view(), name='all_books'),
    path('book/<int:pk>', views.BookDetailedView.as_view(), name='book_detail'),

    # path('search/', BookSearchView.as_view(), name='search_results'),
]
