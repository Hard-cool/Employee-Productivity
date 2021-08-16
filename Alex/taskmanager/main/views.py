from django.shortcuts import render
from .models import Task

# Create your views here.


def index(requests):
    return render(requests, 'main/index.html')

def second_title(requests):
    tasks = Task.objects.order_by("-id")
    return render(requests, 'main/second_title.html', {'title': "Задачи", 'tasks': tasks})

def about_us(requests):
    return render(requests, 'main/about_us.html')

def create_task(requests):
    return render(requests, 'main/create_task.html')

