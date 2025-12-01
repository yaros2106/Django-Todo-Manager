from django.urls import path

from todo_list.views import (
    ToDoListIndexView,
    ToDoListView,
    ToDoListDoneView,
    ToDoDetailView,
    ToDoItemCreateView,
    ToDoItemUpdateView,
    ToDoItemDeleteView,
)

app_name = "todo_list"
urlpatterns = [
    path("", ToDoListView.as_view(), name="index"),
    path("list/", ToDoListIndexView.as_view(), name="list"),
    path("done/", ToDoListDoneView.as_view(), name="done"),
    path("<int:pk>/", ToDoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ToDoItemUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ToDoItemDeleteView.as_view(), name="delete"),
    path("create/", ToDoItemCreateView.as_view(), name="create"),
]
