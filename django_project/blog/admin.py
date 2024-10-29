from django.contrib import admin
from .models.post import Post
from .models.comment import Comment


# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["body", "name", "active", "created_date"]
    list_filter = ["active", "created_date"]
    search_fields = ["body", "name", "email"]
    list_editable = ["active"]
    actions = ["mark_as_approved", "delete_all_inactive"]

    def mark_as_approved(self, request, queryset):
        queryset.update(active=True)
    
    def delete_all_inactive(self, request, queryset):
        all_inactives = Comment.objects.filter(active=False)
        all_inactives.delete()
