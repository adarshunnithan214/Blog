from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.contrib import messages

from .forms import BlogForm
from .models import Blog

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully")

            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogs/create_blog.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs, 3)  # 3 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blogs/blog_list.html', {'page_obj': page_obj})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})


def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this blog")

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully")
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blogs/edit_blog.html', {'form': form})


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog")

    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully")
        return redirect('blog_list')

    return render(request, 'blogs/delete_blog.html', {'blog': blog})