from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q
from .models import create_blog, resources 

class HomeView(TemplateView):
    template_name = "blog/home.html"


def blog_list(request):
    query = request.GET.get('si','')
    if query:
        queryset = (Q(title__icontains=query))
        post = create_blog.objects.filter(queryset).distinct()
    else:
        post = create_blog.objects.all()
    context = {'post':post,'query':query}
    return render(request, 'blog/blog_list.html', context)
        


def blog_detail(request, *args, **kwargs):
    post = get_object_or_404(create_blog, pk=kwargs.get("pk"))
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context) 

class aboutView(TemplateView):
    template_name = "blog/about.html"


def resource_list(request):
    query = request.GET.get('se','')
    if query:
        queryset = (Q(tags__icontains=query))
        post = resources.objects.filter(queryset).distinct()
    else:
        post = resources.objects.all()
    context = {'post':post,'query':query}
    return render(request, 'blog/resource_list.html', context)


def resource_detail(request, *args, **kwargs):
    post = get_object_or_404(resources, pk=kwargs.get("pk"))
    context = {'post': post,}
    return render(request, 'blog/resource_detail.html', context) 