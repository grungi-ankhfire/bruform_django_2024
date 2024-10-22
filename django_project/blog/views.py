from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

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
    #success_url = reverse_lazy("post_list")

    def get_success_url(self):
        post_id = self.object.pk
        return reverse("post_detail", kwargs={"pk": post_id})

    def form_valid(self, form):
        # form.instance.title = form.instance.title.upper()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "New post"
        return context

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

class PostEdit(UpdateView):
    model = Post
    fields = ("author", "title", "text")
    template_name = "blog/post_new.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Edit post"
        return context

class About(TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_count"] = 42512
        context["author_count"] = 25
        return context
