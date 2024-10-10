from dataclasses import fields
from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        widgets = {
            "available": forms.CheckboxInput(attrs={"class": "form-check"})
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 5:
            raise forms.ValidationError("Название комнаты должно содержать не менее 5 символов")
        return name
