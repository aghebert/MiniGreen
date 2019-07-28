from django.db import models


class PostQuerySet(models.QuerySet):
    def get_author_posts(self, username):
        return self.filter(author__user__username=username)

    def get_editor_posts(self, username):
        return self.filter(editor__user__username=username)


class AuthorManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_users_posts(self, username):
        return self.get_queryset().get_author_posts(username)

    def all(self):
        return self.get_queryset()


class EditorManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_users_posts(self, username):
        return self.get_queryset().get_editor_posts(username)
