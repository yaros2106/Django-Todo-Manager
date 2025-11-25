from django.urls import path

from todo_list.views import ToDoListIndexView

app_name = "todo_list"
urlpatterns = [
    path("", ToDoListIndexView.as_view(), name="index"),
]
