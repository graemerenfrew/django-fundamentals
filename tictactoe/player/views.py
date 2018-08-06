from django.shortcuts import render

# Create your views here.


def home(request):
    ''' Lets delegate the creation of the html to the template using the render function'''
    return render(request, "player/home.html")