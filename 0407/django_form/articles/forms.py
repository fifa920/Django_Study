from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=1,
        label='제목',
        help_text='제목을 입력하세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '제목입력'
            }
        )
    )
    class Meta:
        model = Article
        fields = ['title', 'content']