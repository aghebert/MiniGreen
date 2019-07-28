from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_DB/', views.show_data, name="mongoDB")
]