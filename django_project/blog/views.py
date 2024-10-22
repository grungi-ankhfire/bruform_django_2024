from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post

# Create your views here.
# Function-based view
def post_list(request):

    posts = Post.objects.all()

    return render(request, "blog/post_list.html", {"all_posts":posts})

# Class-based view
class PostList(ListView):
    model = Post
    context_object_name = "all_posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

class PostNew(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ("author", "title", "text")
