from django.db import models
from .post import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return self.post.get_absolute_url()
