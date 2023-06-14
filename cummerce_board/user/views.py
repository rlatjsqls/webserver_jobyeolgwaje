from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

from django.utils import timezone


def index(request):
    return render(request, 'board/hompage.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # 로그인
            return redirect(reverse('user:index'))
    return render(request, 'user/register.html', {'form': form})
