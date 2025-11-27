from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

from todo_list.models import ToDoItem


class ToDoListView(ListView):
    template_name = "todo_list/index.html"
    model = ToDoItem
    context_object_name = "todo_items"

    def get_queryset(self):
        return super().get_queryset()[:3]


class ToDoListIndexView(TemplateView):
    template_name = "todo_list/todoitem_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_items = ToDoItem.objects.all()
        context["todo_items"] = todo_items
        return context


class ToDoListDoneView(ListView):
    template_name = "todo_list/done_items.html"
    model = ToDoItem
    context_object_name = "todo_items"

    def get_queryset(self):
        return super().get_queryset().filter(done=True)


class ToDoDetailView(DetailView):
    template_name = "todo_list/todoitem_detail.html"
    model = ToDoItem
    context_object_name = "todo_item"
