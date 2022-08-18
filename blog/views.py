from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

def index(request):
    return render(request, 'index.html')

class PostList(ListView):
    model= Post
    template_name = 'post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"