from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="titlepage"),
    path("search", views.search, name='search'),
    path("New", views.new_page, name ='new_page'),
    path("Edit", views.edit_page, name='edit_page'),
    path("save", views.save_edited_entries, name='save_edited_articles'),
    path("random", views.random_Page, name='random_page'),
]