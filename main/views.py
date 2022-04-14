from django.shortcuts import render
from .models import Task
from .forms import TaskForm

from rest_framework import viewsets
from .serializers import TaskSerialiser


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {
                      "title": "Main page",
                      "header": "to-do list",
                      "tasks": tasks,
                  })


def contacts(request):
    return render(request, 'main/contacts.html')


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/task.html', context)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
