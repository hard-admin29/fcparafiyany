from .models import ModelNews
from django.forms import ModelForm, FileInput, TextInput, Textarea, DateTimeInput


class MediaForm(ModelForm):
    class Meta:
        model = ModelNews
        fields = ["content", "title", "anons", "full_text", "data"]
        widgets = {
            "content": FileInput(attrs={
                "class": "form-control content-media",
                "placeholder": "Виберіть фото або відео",
                "accept": "image/*,video/*"
            }),
            "title":  TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть назву статті"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Напишіть анонс"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Стаття"
            }),
            "data": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Час",
                "type": "datetime-local"
            })
        }