from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

# Create your views here.

#relative import of froms
from .models import Vehicle
from .forms import VehicleForm

def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, 'create_view.html', context)



