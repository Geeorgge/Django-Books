from django import forms
from books.form import ReviewForm
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Review
from django.http import Http404, response
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
import requests

# Create your views here.


class BookListView(ListView):

    #book_list its from the Django module "list.py", 
    # in get_context_object_name, line 109
    #It works to delete the "context_object_name" from this class
    def get_queryset(self):
        return Book.objects.all() 

    

class  BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form']    = ReviewForm()
        return context


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

def review(request, id):
    if request.user.is_authenticated:
        newReview = Review(book_id=id, user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newReview)
        if form.is_valid():
            form.save()
    return redirect(f'/book/{id}')



