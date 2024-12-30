from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
    path('borrowers/', views.BorrowerListCreateView.as_view(), name='borrower-list-create'),
    path('borrowers/<int:pk>/', views.BorrowerRetrieveUpdateDestroyView.as_view(), name='borrower-detail'),
]