# blog/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse

from . models import Post


class HomeListView(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_list = 'post_list'

class BlogDetailView(DetailView):
    model = Post 
    template_name  = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    
class BlogUpdateView(UpdateView):
    model = Post 
    template_name = 'post_edit.html'
    fields = ['title', 'text']
