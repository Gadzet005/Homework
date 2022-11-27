from django.db import models


class Feedback(models.Model):
    text = models.TextField(verbose_name="Текст")
    email = models.EmailField(verbose_name="Почта")
    created_on = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
        )

    class Meta:
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'

    def __str__(self):
        return f"Обращение от {self.email}"
