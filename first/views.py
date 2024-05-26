from django.shortcuts import render
from .models import firstVariety
from django.shortcuts import get_object_or_404


# Create your views here.

def all_first(request):
    first_me = firstVariety.objects.all()
    return render(request, 'first/all_first.html', {'first_me': first_me})

def first_detail(request, first_id):
    first = get_object_or_404(firstVariety, pk=first_id)
    return render(request, 'first/first_detail.html', {'first': first})

