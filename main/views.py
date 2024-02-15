from django.shortcuts import render
from .models import BlogpostModel

def home(request):
    blogpost_objs = BlogpostModel.objects.all()
    context = {
        "blogposts":blogpost_objs
    }
    print(blogpost_objs.image)
    return render(request, 'home.html', context)