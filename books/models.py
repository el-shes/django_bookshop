from django.db import models


class Author(models.Model):
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_first_name + " " + self.author_last_name


class BookLanguage(models.Model):
    LANGUAGES = [('Eng', 'English'), ('Fr', 'French'), ('UA', 'Ukrainian')]
    language_name = models.CharField(max_length=3, choices=LANGUAGES)

    def __str__(self):
        return self.language_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.ManyToManyField(Author)
    book_language = models.ForeignKey(BookLanguage, on_delete=models.CASCADE)
    num_pages = models.PositiveSmallIntegerField()
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title
