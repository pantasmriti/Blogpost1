from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogpostModel
from .forms import BlogPostForm

def home(request):
    blogpost_objs = BlogpostModel.objects.all()
    context = {
        "blogposts":blogpost_objs
    }
    # print(blogpost_objs.image.)
    return render(request, 'home.html', context)


def blogpost_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost_list')
    else:
        form = BlogPostForm()
    return render(request, 'blogpost_create.html', {'form': form})

def blogpost_update(request, pk):
    post = get_object_or_404(BlogpostModel, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogpost_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpost_update.html', {'form': form})

def blogpost_delete(request, pk):
    post = get_object_or_404(BlogpostModel, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogpost_list')
    return render(request, 'blogpost_delete.html', {'post': post})