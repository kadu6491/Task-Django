from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    context = {'forms': form};
    return render(request, 'index.html', context)


