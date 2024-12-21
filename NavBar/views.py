from django.shortcuts import render

# Create your views here.

def logo(req):
    return render(req,'logo.html')
def support(req):
    return render(req,'support.html')
def locations(req):
    return render(req,'locations.html')
def food(req):
    return render(req,'food.html')