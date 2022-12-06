from django import forms

from .models import Feedback
from Core.utils import FormStyleMixin


class FeedbackForm(forms.ModelForm, FormStyleMixin):
    class Meta:
        model = Feedback
        fields = ('text',)
        help_texts = {
            'text': 'Введите ваше сообщение',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }
