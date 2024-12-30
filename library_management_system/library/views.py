from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book, Author, Borrower
from .serializers import BookSerializer, AuthorSerializer, BorrowerSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all().prefetch_related('borrowed_books')
    serializer_class = BorrowerSerializer
    permission_classes = [IsAuthenticated]