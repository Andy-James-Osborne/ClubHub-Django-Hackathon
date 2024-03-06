from django.shortcuts import render, redirect
from .models import User, Events, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    else: 
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect(request, 'login.html')

def event_details(request, slug):
    get_event = Events.object.get(slug=slug)
    get_all_comments = Comment.object.filter(event=get_event)
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        new_comment = Comment(name=name, body=body, event=get_event)
        new_comment.save()
        message.success(request, 'Your comment was successfully uploaded.')
        return redirect('event-details', slug=slug)
    get_event = Events.objects.get(slug=slug)
    context = {
        'event': get_event,
        'comment': get_all_comments,
    }
    return render(request, 'events.html', context)