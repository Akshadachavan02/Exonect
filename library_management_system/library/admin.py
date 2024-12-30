from django.contrib import admin
from .models import Book, Author, Borrower

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'available')
    list_filter = ('author', 'available')
    search_fields = ('title', 'author__name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'return_date')
    list_filter = ('book',)
    search_fields = ('user__username',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Borrower, BorrowerAdmin)