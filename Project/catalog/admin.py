from django.contrib import admin

import catalog.models as CategoryModels


class CatalogBaseAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    list_display_links = ('id', 'name')


class CategoryModelAdmin(CatalogBaseAdmin):
    list_display = ('id', 'name', 'is_published', 'slug', 'weight')
    prepopulated_fields = {'slug': ('name',)}


class TagModelAdmin(CatalogBaseAdmin):
    list_display = ('id', 'name', 'is_published', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ItemModelAdmin(CatalogBaseAdmin):
    list_display = ('id', 'name', 'is_published', 'category')
    filter_horizontal = ('tags',)


admin.site.register(CategoryModels.Item, ItemModelAdmin)
admin.site.register(CategoryModels.Category, CategoryModelAdmin)
admin.site.register(CategoryModels.Tag, TagModelAdmin)
