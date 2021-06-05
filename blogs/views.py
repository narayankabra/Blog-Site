from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects
    return render(request, 'blogs/index.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog_detail})
