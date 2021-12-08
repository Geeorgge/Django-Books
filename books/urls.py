from books.models import Book
from django.urls import path
from . import views
import books
 

urlpatterns = [
    path('',                  views.BookListView.as_view(), name='book.all'),
    path('<int:pk>',          views.BookDetailView.as_view(), name="book.show"),
    path('<int:id>/review',   views.review, name="book.review"),
    path('<str:author>',      views.author, name="author.books"),

]
