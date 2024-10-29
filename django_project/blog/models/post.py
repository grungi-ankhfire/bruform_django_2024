from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__lte=timezone.now())

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedPostsManager()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def __str__(self):
        return self.title
