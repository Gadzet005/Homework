from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем ко всем полям стиль по умолчанию
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Feedback
        fields = ("email", "text")
        help_texts = {
            "text": "Введите ваше сообщение",
            "email": "Введите вашу почту, чтобы мы могли связаться с вами"
        }
        widgets = {
            "text": forms.Textarea(attrs={"cols": 60, "rows": 5}),
        }
