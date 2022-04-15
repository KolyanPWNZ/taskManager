from .models import Task, Post
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "aria-describedby": "titleHelp",
                "placeholder": "Drink a coffee",
                "type": "text"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "description",
                "aria-describedby": "descriptionHelp",
                "placeholder": "Make yourself some coffee",
            })
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'posted', 'deleted']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "aria-describedby": "titleHelp",
                "placeholder": "Your post",
                "type": "text"
            }),
            "posted": TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "aria-describedby": "titleHelp",
                "type": "date'"
            })
        }
