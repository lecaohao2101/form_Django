from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_create')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'content': forms.TextInput(attrs={'class': 'content'})
        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'title'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'content'}))
    cc = forms.BooleanField()
