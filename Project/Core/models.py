from django.db import models


# Этот класс нужен для хранения тех полей, которые
# используются в нескольких моделях, но не во всех
# (поэтому их нельзя добавить в абстрактный класс)
class ProjectBaseFields:
    id = models.BigAutoField(
            verbose_name='ID', auto_created=True, primary_key=True,
            serialize=False,
            )
    is_published = models.BooleanField(
            verbose_name='Опубликовано', default=True
            )
    name = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(verbose_name='URL', max_length=200, unique=True)


class ProjectBaseModel(models.Model):
    class Meta:
        abstract = True

    id = ProjectBaseFields.id
    is_published = ProjectBaseFields.is_published
    name = ProjectBaseFields.name

    def __str__(self):
        return self.name
