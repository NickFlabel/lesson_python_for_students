from django import forms
from my_app.models import BBoard

class BBoardForm(forms.ModelForm):
    class Meta:
        model = BBoard
        fields = "__all__"
