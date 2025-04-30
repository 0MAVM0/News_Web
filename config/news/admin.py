from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "created_at", "published_at", "updated_at")
    list_filter = ("status", "category")
    search_fields = ("title", "body")
    prepopulated_fields = { "slug" : ("title",) }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
