from django.contrib import admin

import catalog.models as CatalogModels


class CatalogBaseAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    list_display_links = ('name',)


@admin.register(CatalogModels.Item)
class ItemModelAdmin(CatalogBaseAdmin):
    fields = (
        'name', 'is_published', 'is_on_main', 'text', 'category', 'tags',
        'preview', 'image_tmb'
        )
    list_display = (
        'name', 'is_published', 'is_on_main', 'category', 'image_tmb'
        )
    list_editable = ('is_published', 'is_on_main')
    filter_horizontal = ('tags',)
    readonly_fields = ('image_tmb',)

    class ItemGalleryInline(admin.TabularInline):
        model = CatalogModels.ImageGallery
        extra = 0
        readonly_fields = ('image_tmb',)
    inlines = (ItemGalleryInline, )


@admin.register(CatalogModels.Category)
class CategoryModelAdmin(CatalogBaseAdmin):
    fields = ('name', 'is_published', 'slug', 'weight')
    list_display = ('name', 'is_published', 'slug', 'weight')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CatalogModels.Tag)
class TagModelAdmin(CatalogBaseAdmin):
    fields = ('name', 'is_published', 'slug')
    list_display = ('name', 'is_published', 'slug')
    prepopulated_fields = {'slug': ('name',)}
