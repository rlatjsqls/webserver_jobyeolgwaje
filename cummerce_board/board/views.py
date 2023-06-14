from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'board/homepage.html')
