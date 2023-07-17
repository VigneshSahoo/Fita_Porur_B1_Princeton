from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


classrooms = [
    {'id': 1, 'name': 'Harvard'},
    {'id': 2, 'name': 'Nalanda'},
    {'id': 3, 'name': 'Princeton'},
    {'id': 4, 'name': 'Imperial'},
    {'id': 5, 'name': 'Oxford'},
    {'id': 6, 'name': 'Fita'},
]


def welcome(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        context = {'username': username}
        return render(request,
                      'welcome.html',
                      context)
    else:
        return render(request, 'input.html')


def index(request):
    return render(request,
                  'index.html')


def rooms(request):
    context = {'classrooms': classrooms}
    return render(request,
                  'rooms.html',
                  context)


def pages(request, pk):
    room = None
    for i in classrooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'room_page.html', context)


class CustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


def register(request):
    form = CustomForm()
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    loginform = CustomForm
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.error(request, "Invalid Login!")
    context = {'login': loginform}
    return render(request, 'login.html', context)


def dashboard(request):
    context = {}
    return render(request,
                  'dash.html',
                  context)
