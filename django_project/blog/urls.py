from django.urls import path
from . import views

urlpatterns = [
    path("old/", views.post_list, name="old_post_list"),
    path("", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
    path("post/new", views.PostNew.as_view(), name="post_new"),
    path("post/<int:pk>/delete", views.PostDelete.as_view(), name="post_delete"),
    path("post/<int:pk>/edit", views.PostEdit.as_view(), name="post_edit"),
    path("about", views.About.as_view(), name="about"),
]