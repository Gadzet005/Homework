# Generated by Django 3.2.16 on 2022-11-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_item_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/preview/%Y/%m', verbose_name='превью'),
        ),
    ]
