from django.contrib import admin

# Register your models here.

from .models import Post, Author, Editor

admin.site.register(Post)
admin.site.register(Editor)
admin.site.register(Author)
