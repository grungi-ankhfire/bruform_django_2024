from django.urls import path
from . import views

urlpatterns = [
    path("old/", views.post_list, name="old_post_list"),
    path("", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
]