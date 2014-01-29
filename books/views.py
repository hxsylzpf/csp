from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from books.models import Publisher, Author, Book
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from django.views.generic.base import View
from django import forms

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books':books, 'query':q})
    return render(request, 'books/search_form.html', {'errors': errors})

def search_form(request):
    return render(request, 'books/search_form.html')