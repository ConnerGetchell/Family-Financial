from .models import MemoComment, Memo
from django import forms

class NewMemoForm(forms.ModelForm):
    message = forms.CharField(
        widget = forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Tell your family about your finances.'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000'
    )

    class Meta:
        model = Memo
        fields = ['subject', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemoComment
        fields = ['comment']


