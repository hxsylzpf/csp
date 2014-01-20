from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice, Book
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from django.views.generic.base import View
from django import forms

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def search_form(request):
    return render(request, 'books/search_form.html')