from django.db import models

from catalog.models import Item
from Users.models import User


RATING_CHOICES = (
    (1, 'Ненависть'),
    (2, 'Неприязнь'),
    (3, 'Нейтрально'),
    (4, 'Обожание'),
    (5, 'Любовь'),
)


class ItemRatingManager(models.Manager):
    def get_rating_of_item(self, item):
        return (
            self.get_queryset()
            .filter(item=item)
            .aggregate(
                item_rating_avg=models.Avg('rating'),
                item_rating_num=models.Count('user')
                )
            )


class ItemRating(models.Model):
    item = models.ForeignKey(
        Item, verbose_name='товар', on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.CASCADE
        )
    rating = models.SmallIntegerField('оценка', choices=RATING_CHOICES)

    objects = ItemRatingManager()

    class Meta:
        unique_together = ('item', 'user',)

    def __str__(self):
        return str(self.rating)
