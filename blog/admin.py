from django.contrib import admin

# Register your models here.
from .models import Post

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'author')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
