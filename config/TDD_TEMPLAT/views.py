from django.shortcuts import render

# Create your views here.
def tdd(request):
    return render(request , 'show.html')