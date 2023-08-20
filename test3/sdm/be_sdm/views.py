from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import FileUpload
from .forms import FileUploadForm
import datetime

def login_user(request):
    return render(request, 'authenticate/login.html')

def proses_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('sdm:home')
        else:
            messages.error(request, ("Username / Password Salah !!!"))
            return redirect('sdm:login')
    else:
        return render(request, 'authenticate/login.html')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Berhasil Registrasi'))
            return redirect('sdm:login')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register.html', {
        'form' : form,
    })

def logout_user(request):
    logout(request)
    return redirect('sdm:login')

@login_required()
def home(request):
    user = User.objects.all()
    data = {
        'user':user,
    }
    return render(request, 'home.html', data)

@login_required()
def uploadData(request):
    if request.method == 'POST':
        user = request.user.username
        activity = request.POST['activity']
        files = request.FILES.getlist('image')
        for file in files:
            data = FileUpload.objects.create(
                user = user,
                activity=activity,
                image=file,
            )
    form = FileUploadForm
    data = {
        'form': form,
    }
    return render(request, 'upload.html', data)

@login_required()
def dataImage(request):
    pictures = FileUpload.objects.all()
    data = {
        'pictures': pictures,
    }
    return render(request, 'dataImage.html', data)

@login_required()
def detailImage(request):
    if request.method == 'GET':
        id = request.GET['id']
        detail = FileUpload.objects.get(id=id)
        data = detail.image.url
    return HttpResponse(data)
    
