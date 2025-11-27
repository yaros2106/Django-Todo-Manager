from django.urls import path

from todo_list.views import (
    ToDoListIndexView,
    ToDoListView,
    ToDoListDoneView,
    ToDoDetailView,
)

app_name = "todo_list"
urlpatterns = [
    path("", ToDoListView.as_view(), name="index"),
    path("list/", ToDoListIndexView.as_view(), name="todoitem_list"),
    path("done/", ToDoListDoneView.as_view(), name="done"),
    path("<int:pk>/", ToDoDetailView.as_view(), name="detail"),
]
