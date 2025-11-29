from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import Textarea

from todo_list.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title",)
        # widgets = {
        #     "title": Textarea(attrs={"cols": 30, "rows": 5}),
        # }
        labels = {
            "title": _("Task title"),
        }
