# coding: utf-8
from django.shortcuts import render

from project.core.models import Post
from django.views.generic import ListView, DetailView, CreateView

class PostsListView(ListView):  # представление в виде списка
    model = Post                   # модель для представления

class PostDetailView(DetailView):  # детализированное представление модели
    model = Post

class PostFormView(CreateView):  # s
    model = Post
