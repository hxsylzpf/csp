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
#from .forms import MyForm

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
    
class ContactForm(forms.Form):
    # https://docs.djangoproject.com/en/1.6/ref/forms/fields/
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    
# Create your views here.
class MyFormView(View):
    #form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
    
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
    
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
    
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('myview result')
    
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'latest_book_list'
    template_name = 'polls/books.html'
    
    def get_queryset(self):
        return Book.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
    def head(self, *args, **kwargs):
        last_book = self.get_queryset()
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response
    
class AboutView(generic.TemplateView):
    template_name = "polls/about.html"

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        #return Poll.objects.order_by('-pub_date')[:5]
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


"""
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {'latest_poll_list': latest_poll_list,})
    #return HttpResponse(template.render(context))

    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    #try:
    #    poll = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})
    #return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
"""
