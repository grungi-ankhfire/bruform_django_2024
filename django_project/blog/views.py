from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ModelFormMixin
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from django.db.models import Q
from .models.post import Post
from .forms import CommentForm

# Create your views here.
# Function-based view
def post_list(request):

    posts = Post.objects.all()

    return render(request, "blog/post_list.html", {"all_posts":posts})

# Class-based view
class PostList(ListView):
    # model = Post
    context_object_name = "all_posts"
    queryset = Post.published.all()

class PostDraftList(ListView):
    # template_name = "blog/post_list.html"
    context_object_name = "all_posts"
    queryset = Post.objects.filter(Q(published_date__gt=timezone.now()) | Q(published_date__isnull=True))


class PostDetail(ModelFormMixin, DetailView):
    model = Post
    form_class = CommentForm
    context_object_name = "post"

    def post(self, request, pk):
        form = self.get_form()
        self.object = self.get_object()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(active=True)
        return context


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
        context["post_count"] = Post.objects.count()
        # context["author_count"] = User.objects.count()  # Compte tous les utilisateurs
        context["author_count"] = Post.objects.values("author").distinct().count()  # Compte les auteurs liés à un Post
        # context["author_count"] = User.objects.filter(post__isnull=False).distinct().count()

        # context["author_post_count"] = Post.objects.values("author").annotate(post_count=Count("author")).order_by("-post_count")
        context["author_count"] = Post.objects.values("author").annotate(Count("id")).count()
        return context

class PostPublish(RedirectView):
    pattern_name = "post_detail"

    def get_redirect_url(self, *args, **kwargs):
        # blog_post = Post.objects.get(pk=kwargs["pk"])
        blog_post = get_object_or_404(Post, pk=kwargs["pk"])
        blog_post.publish()

        return super().get_redirect_url(*args, **kwargs)
    