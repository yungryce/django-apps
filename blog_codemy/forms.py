from django import forms
from .models import Reg

class Formsk(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('title', 'title_tag')

    widgets = {
        'title': forms.TextInput(attrs={'class' : 'form-control'}),
        'title_tag': forms.TextInput(attrs={'class' : 'form-control'}),
        'author': forms.Select(attrs={'class' : 'form-control'}),
        'title': forms.Textarea(attrs={'class' : 'form-control'})
    }