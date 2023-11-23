from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from .models import Blogs


def index(request):

    posts = Blogs.objects.all()

    return render(request,"index.html" , {'posts': posts})

