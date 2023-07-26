from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Rooms, StudentForm, Students


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
    a = Students.objects.all()
    b = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': a, 'b': b}
    return render(request, 'index.html', context)


@login_required(login_url='login_page')
def rooms(request):
    classrooms = Rooms.objects.all()
    context = {'classrooms': classrooms}
    return render(request,
                  'rooms.html',
                  context)


def pages(request, pk):
    classrooms = Rooms.objects.all()
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
        else:
            messages.error(request, 'Registration Failed')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.error(request, "Invalid Login!")
    context = {}
    return render(request, 'login.html', context)


def logoutfunc(request):
    logout(request)
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dash.html',)
