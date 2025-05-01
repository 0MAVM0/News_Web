from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Izoh yozing...',
        }),
        label='',
    )

    class Meta:
        model = Comment
        fields = ['comment']

