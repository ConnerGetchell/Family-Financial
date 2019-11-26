from .models import MemoComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemoComment
        fields = ('comment',)
