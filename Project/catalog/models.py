from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail

from Core.models import ProjectBaseFields, ProjectBaseModel
from Core.validators import AmazingTextValidator


class Item(ProjectBaseModel):
    text = RichTextField(
        verbose_name='описание',
        validators=[AmazingTextValidator('превосходно', 'роскошно')],
        help_text='Должно создержать слова превосходно или роскошно'
        )
    category = models.ForeignKey(
        'Category', verbose_name='категория', on_delete=models.CASCADE
        )
    tags = models.ManyToManyField('Tag', verbose_name='тег')
    preview = models.ImageField(
        verbose_name='превью', upload_to='uploads/preview/%Y/%m', null=True,
        blank=True
        )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def get_absolute_url(self):
        return reverse('catalog:item_detail', kwargs={'item_id': self.pk})

    ''' Метод, масштабирующий превью до размера 300x300 '''
    def image_tmb(self):
        if self.preview:
            img = get_thumbnail(
                self.preview, '300x300', crop='center', quality=51
                )
            return mark_safe(f'<img src="{img.url}">')
        return 'Нет изображения'


class ImageGallery(models.Model):
    upload = models.ImageField(
        verbose_name='картинка', upload_to='uploads/gallery/%Y/%m'
        )
    item = models.ForeignKey(
        "Item", verbose_name='товар', on_delete=models.CASCADE
        )

    def __str__(self) -> str:
        return f'Картинка №{self.pk}'


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
