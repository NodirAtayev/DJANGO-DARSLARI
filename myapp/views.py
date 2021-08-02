from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    names = ['BAHROM', 'SOBIR', 'BOTIR']
    name = 'JANOB RASUL'
    return render(request, 'index.html', {'ism': name, 'ismlar': names})

def goodbye(request):
    return HttpResponse("XAYR ALVIDO BEGUBOR YOSHLIGIM")

def ism(request):
    return HttpResponse("<font color= 'green'> <h1> SaLoM BaXrOm AkA  </h1></font color>")

