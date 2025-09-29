from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def menu(request):
    return render(request, 'myapp/menu.html')

def delivery(request):
    return render(request, 'myapp/delivery.html')

def trackorder(request):
    return render(request, 'myapp/trackorder.html')