from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def funfact(request):
    return render(request, 'main/funfact.html')
def wahkokbisa(request):
    return render(request, 'main/wahkokbisa.html')
def howtouse(request):
    return render(request, 'main/howtouse.html')
def product(request):
    return render(request, 'main/product.html')