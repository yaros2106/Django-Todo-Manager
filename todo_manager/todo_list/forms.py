from django import forms
from django.forms import Textarea

from todo_list.models import ToDoItem


class ToDoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = (
            "title",
            "description",
        )
        widgets = {
            "description": Textarea(attrs={"cols": 30, "rows": 5}),
        }
        labels = {
            "title": "Task title",
        }


class ToDoItemUpdateForm(forms.ModelForm):
    class Meta(ToDoItemCreateForm.Meta):
        fields = (
            "title",
            "description",
            "done",
        )
