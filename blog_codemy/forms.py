from django import forms
from .models import Reg

class Postform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('title', 'title_tag', 'author', 'body')
        # to replace foields on template
        labels = {
        'title': 'Title',
        'title_tag': 'Tag',
        'author': 'Writer',
        'body': 'Text',
        }


        #doesnt work. review
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Post Title'}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
        }


class Editform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('title', 'title_tag', 'body')
    
        labels = {
        'title': 'Title', 
        'title_tag': 'Tag',
        # 'author': 'Writer',
        'body': 'Text',
        }


        #doesnt work. review
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Post Title'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
        }