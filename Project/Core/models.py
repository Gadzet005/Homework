from django.db import models


# Этот класс нужен для хранения тех полей, которые
# используются в нескольких моделях, но не во всех
# (поэтому их нельзя добавить в абстрактный класс)
class ProjectBaseFields:
    slug = models.SlugField(verbose_name='URL', max_length=200, unique=True)


class ProjectBaseModel(models.Model):
    class Meta:
        abstract = True

    is_published = models.BooleanField(
            verbose_name='Опубликовано', default=True
            )
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return self.name
