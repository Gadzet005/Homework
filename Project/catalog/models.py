from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse

from Core.models import ProjectBaseFields, ProjectBaseModel, ProjectBaseManager
from Core.validators import AmazingTextValidator
from .utils import get_image_thumbnail


class ItemManager(ProjectBaseManager):
    def published(self):
        return (
            super().published()
            .filter(category__is_published=True)
            .select_related('category')
            .prefetch_related(models.Prefetch('tags', Tag.objects.published()))
            .only('name', 'text', 'category__name', 'preview')
        )

    def on_main(self):
        return self.published().filter(is_on_main=True)


class Item(ProjectBaseModel):
    is_on_main = models.BooleanField(verbose_name='На главной', default=False)
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

    objects = ItemManager()

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def get_absolute_url(self):
        return reverse('catalog:item_detail', kwargs={'item_id': self.pk})

    def image_tmb(self):
        return get_image_thumbnail(self.preview)

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class ImageGallery(models.Model):
    upload = models.ImageField(
        verbose_name='картинка', upload_to='uploads/gallery/%Y/%m'
        )
    item = models.ForeignKey(
        'Item', verbose_name='товар', on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'галлерея'

    def __str__(self) -> str:
        return f'Картинка №{self.pk}'

    def image_tmb(self):
        return get_image_thumbnail(self.upload)

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
