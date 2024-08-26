# from django.shortcuts import render
from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'app/about.html')

def main(request):
    return render(request, 'app/main.html')

def contacts(request):
    return render(request, 'app/contacts.html')

# '''
# открыть страничку по адресу
# http://127.0.0.1:8000/pages/page1
# http://127.0.0.1:8000/pages/page2
# http://127.0.0.1:8000/pages/page2
# '''