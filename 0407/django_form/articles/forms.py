from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']