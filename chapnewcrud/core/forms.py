from django import forms
from .models import Core



class PostForm(forms.ModelForm):
    class Meta:
        Model = Core
        fields = "__all__"