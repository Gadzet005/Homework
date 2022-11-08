from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail


def get_image_thumbnail(upload, size_string='300x300'):
    ''' Метод, масштабирующий изображение до размера size_string '''

    if upload:
        img = get_thumbnail(
            upload, size_string, crop='center', quality=99
            )
        return mark_safe(f'<img src="{img.url}">')
    return 'Нет изображения'
