from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def stock(request):
    return render(request, 'stock.html')  

def sales(request):
    return render(request, 'sales.html')  

def customers(request):
    return render(request, 'customers.html')    

def suppliers(request):
    return render(request, 'suppliers.html')

def reports(request):
    return render(request, 'reports.html')