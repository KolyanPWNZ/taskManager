from django.shortcuts import render
from .models import Task, Post
from .forms import TaskForm, PostForm

from rest_framework import viewsets
from .serializers import TaskSerialiser, PostSerialiser

from django.http import HttpResponseRedirect


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


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    if request.method == 'GET':
        form = PostForm(request.GET)
        if form.is_valid():
            print(form)

    form = PostForm()
    posts = Post.objects.order_by('-id')
    context = {
        'form': form,
        "title": "Publication",
        "header": "My publication",
        "posts": posts,
    }
    return render(request, 'main/post.html', context)



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialiser