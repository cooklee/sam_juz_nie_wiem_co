from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from accounts.forms import LoginForm, RegistrationForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form_with_python_form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return HttpResponse("błędne dane logowania")


class LogOut(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class RegistrationUserView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'form_with_python_form.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('index')
        return render(request, 'form_with_python_form.html', {'form': form})
