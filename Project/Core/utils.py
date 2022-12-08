from django import forms


class FormStyleMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Применяем ко всем полям стиль по умолчанию
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
