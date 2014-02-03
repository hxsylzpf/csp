from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from geocrowd.forms import GeocrowdForm
from geocrowd.models import Geocrowd
        
        
# Create your views here.
def geocrowd(request):
    if request.method == 'POST':
        # http request
        a = Geocrowd.objects.get(pk=1)
        form = GeocrowdForm(request.POST, instance=a)
          
        if form.is_valid():
            # update database  
            form.save(commit=True)
            data = form.cleaned_data
            url = "http://137.135.57.140/param/?"
            url = url + "dataset=" + data['datasets']
            url = url + "&eps=" + data['budgets']
            url = url + "&algo=" + data['algos']
            url = url + "&mar=" + data['mars']
            url = url + "&arf=" + data['ars']
            url = url + "&mtd=" + data['mtds']
            url = url + "&utl=" + data['us']
            url = url + "&rebuild=1"
        
            return HttpResponseRedirect(url)
    else:
        a = Geocrowd.objects.get(pk=1)
        form = GeocrowdForm(instance=a)
    return render(request, 'geocrowd_form.html', {'form':form})