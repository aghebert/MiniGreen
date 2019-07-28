from django.urls import path

from .views import posts_list, posts_detail, posts_create, posts_update, posts_delete

urlpatterns = [
    path('', posts_list),
    path('create/', posts_create),
    path('<slug>/update/', posts_update),
    path('<slug>/delete/', posts_delete),
    path('<slug>/', posts_detail)
]
