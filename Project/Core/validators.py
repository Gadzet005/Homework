from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class AmazingTextValidator:
    def __init__(self, *words):
        try:
            self.words = set(words)

            words_for_pattern = '|'.join(self.words)
            self.pattern = re.compile(fr'\b({words_for_pattern})\b', re.I)
        except TypeError:
            raise TypeError('Валидатор получил аргумент с неправильным типом')

    def __call__(self, text):
        if self.words and self.pattern.search(text) is None:
            raise ValidationError(
                f'Текст должен содержать одно из слов: {', '.join(self.words)}'
                )

        return text
