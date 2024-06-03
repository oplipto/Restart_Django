from django.shortcuts import render
from .models import firstVariety
from django.shortcuts import get_object_or_404
from .models import firstVariety
from .forms import firstVarietyForm 
from .models import Store



# Create your views here.

def all_first(request):
    first_me = firstVariety.objects.all()
    return render(request, 'first/all_first.html', {'first_me': first_me})

def first_detail(request, first_id):
    first = get_object_or_404(firstVariety, pk=first_id)
    return render(request, 'first/first_detail.html', {'first': first})

def first_store_review(request):
    stores = None
    if request.method == 'POST':
        form = firstVarietyForm(request.POST)
        if form.is_valid():
            first_variety = form.cleaned_data.get('first_variety')
            stores = Store.objects.filter(first_varieties = first_variety)
    else:
        form = firstVarietyForm()

    return render(request, 'first/first_stores.html', {'stores' : stores, 'form' : form})