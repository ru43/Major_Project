from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login




def home(request):
    return render(request,'courier_page.html')
