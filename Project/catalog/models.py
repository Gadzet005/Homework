from django.db import models

from Core.models import ProjectBaseFields, ProjectBaseModel
from Core.validators import AmazingTextValidator


class Item(ProjectBaseModel):
    text = models.TextField(
        verbose_name='Описание',
        validators=[AmazingTextValidator('превосходно', 'роскошно')]
        )
    category = models.ForeignKey(
        'Category', verbose_name='Категория', on_delete=models.CASCADE
        )
    tags = models.ManyToManyField('Tag', verbose_name='Тег')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(ProjectBaseModel):
    slug = ProjectBaseFields.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(ProjectBaseModel):
    slug = ProjectBaseFields.slug
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
