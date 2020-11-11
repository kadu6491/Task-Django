from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.


@login_required(login_url="login")
def index(request):
    todos = Task.objects.all()

    form = PostTask()

    if request.method == 'POST':
        form = PostTask(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'todos': todos, 'form': form}
    return render(request, 'todo.html', context)


@login_required(login_url="login")
def update(request, pk):
    ups = Task.objects.get(id=pk)

    form = PostTask(request.POST, instance=ups)

    if 'com' in request.POST:
        ups.completed = True
        ups.save()
        return redirect('/')

    if 'com2' in request.POST:
        ups.completed = False
        ups.save()
        return redirect('/')


    # if request.method == 'POST':
    #     form = PostTask(request.POST, instance=ups)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    context = {'form':form, 'ups':ups}

    return render(request, 'update.html', context)


