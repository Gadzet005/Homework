from django.db import models

from Users.models import User


class Feedback(models.Model):
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey(
        User, verbose_name="Создатель", on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
        )

    class Meta:
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'

    def __str__(self):
        return f"Обращение от {self.user.nickname}"
