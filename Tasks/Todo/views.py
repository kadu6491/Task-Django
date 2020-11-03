from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def index(request):
    todos = Task.objects.all();

    form = PostTask()

    if request.method == 'POST':
        form = PostTask(request.POST)
        if form.is_valid():
            form.save()

    context = {'todos': todos, 'form': form}
    return render(request, 'todo.html', context)


