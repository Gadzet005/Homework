from django.contrib import admin

import catalog.models as CatalogModels


class CatalogBaseAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    list_display_links = ('id', 'name')


@admin.register(CatalogModels.Item)
class ItemModelAdmin(CatalogBaseAdmin):
    fields = ('name', 'is_published', 'text', 'category', 'tags')
    list_display = ('id', 'name', 'is_published', 'category')
    filter_horizontal = ('tags',)


@admin.register(CatalogModels.Category)
class CategoryModelAdmin(CatalogBaseAdmin):
    fields = ('name', 'is_published', 'slug', 'weight')
    list_display = ('id', 'name', 'is_published', 'slug', 'weight')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CatalogModels.Tag)
class TagModelAdmin(CatalogBaseAdmin):
    fields = ('name', 'is_published', 'slug')
    list_display = ('id', 'name', 'is_published', 'slug')
    prepopulated_fields = {'slug': ('name',)}
