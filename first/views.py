from django.shortcuts import render

# Create your views here.

def all_first(request):
    return render(request, 'first/all_first.html')

