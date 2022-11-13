from django.db import models


class ProjectBaseFields:
    '''
    Этот класс нужен для хранения тех полей, которые
    используются в нескольких моделях, но не во всех,
    поэтому их нельзя добавить в базовый класс
    '''

    slug = models.SlugField(verbose_name='URL', max_length=200, unique=True)


class ProjectBaseManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .order_by('name')
            .only('name')
        )


class ProjectBaseModel(models.Model):
    is_published = models.BooleanField(
            verbose_name='опубликовано', default=True
            )
    name = models.CharField(verbose_name='название', max_length=150)

    objects = ProjectBaseManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
