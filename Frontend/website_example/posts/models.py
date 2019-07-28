from django.db import models
from django.conf import settings

from .managers import AuthorManager, EditorManager

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    editor = models.ForeignKey(
        'Editor', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField()
    slug = models.SlugField(unique=True)
    comments = models.IntegerField(default=0)

    authors = AuthorManager()
    editors = EditorManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/posts/{}/".format(self.slug)

    def get_update_url(self):
        return "/posts/{}/update/".format(self.slug)

    def get_delete_url(self):
        return "/posts/{}/delete/".format(self.slug)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username


class Editor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
