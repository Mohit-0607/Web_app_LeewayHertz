from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name='home'),
    path("add_movie", views.add_movie, name='add_movie'),
    path("show_movie", views.show_movie, name='show_movie')
]
