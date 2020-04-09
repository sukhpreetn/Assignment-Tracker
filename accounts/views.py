from django.conf import settings
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView


def signup_view(request):
    return  render(request,'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('tracker:home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'tracker/home.html')