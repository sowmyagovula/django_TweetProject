from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'image']
        # widgets = {
        #     'text': forms.Textarea(attrs={'placeholder': 'What\'s happening?', 'rows': 3}),
        # }
        # labels = {
        #     'content': '',
        # }