from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
    
def event_details(request):
    return render(request, 'events.html')

def logout_user(request):
    return render(request, 'logout.html')