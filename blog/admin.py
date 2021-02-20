from django.contrib import admin
from .models import Blog, BlogType


@admin.register(BlogType)
class BlogType(admin.ModelAdmin):
    list_display = ('id',"type_name")
    ordering = ('id', )

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('id','title', "blog_type", "updated_time","create_time", "author")

