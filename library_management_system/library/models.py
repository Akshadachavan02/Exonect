from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.user.username