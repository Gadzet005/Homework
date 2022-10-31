from django.db import models


class ProjectBaseFields:
    '''
    Этот класс нужен для хранения тех полей, которые
    используются в нескольких моделях, но не во всех,
    поэтому их нельзя добавить в абстрактный класс
    '''

    slug = models.SlugField(verbose_name='URL', max_length=200, unique=True)


class ProjectBaseModel(models.Model):
    is_published = models.BooleanField(
            verbose_name='Опубликовано', default=True
            )
    name = models.CharField(verbose_name='Название', max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
