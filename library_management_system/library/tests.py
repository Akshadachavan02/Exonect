from django.test import TestCase
from .models import Book, Author, Borrower

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author.name, "Test Author")

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Another Author")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Another Author")

class BorrowerModelTest(TestCase):
    def setUp(self):
        self.borrower = Borrower.objects.create(name="Test Borrower")

    def test_borrower_creation(self):
        self.assertEqual(self.borrower.name, "Test Borrower")