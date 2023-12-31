from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="titlepage"),
    path("search", views.search, name='search'),
    path("experiment", views.experiment, name="experiment")
]