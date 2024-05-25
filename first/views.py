from django.shortcuts import render
from .models import firstVariety


# Create your views here.

def all_first(request):
    first_me = firstVariety.objects.all()
    return render(request, 'first/all_first.html', {'first_me': first_me})

