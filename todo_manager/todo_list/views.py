from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from todo_list.models import ToDoItem


class ToDoListIndexView(TemplateView):
    template_name = "todo_list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_items = ToDoItem.objects.all()
        context["todo_items"] = todo_items
        return context
