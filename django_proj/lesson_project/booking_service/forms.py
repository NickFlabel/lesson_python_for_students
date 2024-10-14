from cProfile import label
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


class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Вы уверены, что хотите удалить комнату?")


class AvailabilityForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={"class": "my-class"}), label="Дата начала",)
    end_date = forms.DateField(widget=forms.DateInput(attrs={"class": "my-class"}), label="Дата окончания",)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Дата начала не может быть позже даты окончания")
        return cleaned_data
