from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail

from Core.models import ProjectBaseFields, ProjectBaseModel
from Core.validators import AmazingTextValidator


class Item(ProjectBaseModel):
    text = models.TextField(
        verbose_name='описание',
        validators=[AmazingTextValidator('превосходно', 'роскошно')],
        help_text='Должно создержать слова превосходно или роскошно'
        )
    category = models.ForeignKey(
        'Category', verbose_name='категория', on_delete=models.CASCADE
        )
    tags = models.ManyToManyField('Tag', verbose_name='тег')
    upload = models.ImageField(
        verbose_name='превью', upload_to='uploads/%Y/%m'
        )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def get_absolute_url(self):
        return reverse('catalog:item_detail', kwargs={'item_id': self.pk})

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.get_img.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Tag(ProjectBaseModel):
    slug = ProjectBaseFields.slug

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(ProjectBaseModel):
    slug = ProjectBaseFields.slug
    weight = models.PositiveSmallIntegerField(verbose_name='вес', default=100)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
