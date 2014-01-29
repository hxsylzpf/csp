from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from geocrowd.forms import GeocrowdForm
        
        
# Create your views here.
def geocrowd(request):
    if request.method == 'POST':
        form = GeocrowdForm(request.POST)
        return HttpResponseRedirect('about.html')
    else:
        form = GeocrowdForm()
    return render(request, 'geocrowd_form.html', {'form':form})