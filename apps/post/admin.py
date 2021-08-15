from django.contrib import admin
from apps.post.models import Post

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
