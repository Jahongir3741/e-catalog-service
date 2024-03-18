from django.contrib import admin
from .models import Fond, Category, Mtv, Region, Language, Format, Genre, Serial, Uzmtrk


@admin.register(Fond)
class FondAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['fond', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Mtv)
class MtvAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Serial)
admin.site.register(Uzmtrk)
