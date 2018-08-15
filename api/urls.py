from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_todo, name="add-todo"),
    path('delete/', views.delete_todo, name="delete-todo"),
    path('deleteAll/', views.delete_all, name="delete-all-todo"),
    path('update/', views.update_todo, name="update-todo"),
    path('getAll/', views.get_todos, name="get-all")
]
