from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from geocrowd.forms import GeocrowdForm
from geocrowd.models import Geocrowd
        
        
# Create your views here.
def geocrowd(request):
    
    
    try:
        a = Geocrowd.objects.get(pk=1)
    except:
        a = None
    
    if request.method == 'POST':
        # http request
        if a:
            form = GeocrowdForm(request.POST, instance=a)
        else:
            form = GeocrowdForm(request.POST)
          
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
            url = url + "&cost=" + data['costs']
            url = url + "&rebuild=1"
        
            return HttpResponseRedirect(url)
    else:
        if a:
            form = GeocrowdForm(instance=a)
        else:
            form = GeocrowdForm()
    return render(request, 'geocrowd_form.html', {'form':form})