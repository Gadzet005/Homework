# Generated by Django 3.2.16 on 2022-11-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20221108_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'verbose_name': 'картинка', 'verbose_name_plural': 'галлерея'},
        ),
        migrations.AddField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='На главной'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='upload',
            field=models.ImageField(upload_to='uploads/gallery/%Y/%m', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/preview/%Y/%m', verbose_name='превью'),
        ),
    ]
