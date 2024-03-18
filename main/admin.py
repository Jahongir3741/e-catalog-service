from django.contrib import admin
from .models import Information, Cadre, Poster
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from .resources import InformationAdminResource


@admin.register(Poster)
class Poster(admin.ModelAdmin):
    list_display = ['image']
    search_fields = ['image']


@admin.register(Information)
class InformationAdmin(ImportExportModelAdmin):
    list_display = ['fond', 'category', 'genre', 'poster', 'get_mtv', 'get_region', 'get_formats', 'name', 'mtv_index', 'color', 'duration', 'year']
    search_fields = ['name', 'mtv_index', 'year']
    autocomplete_fields = ['fond', 'category', 'genre', 'mtv', 'formats', 'language', 'poster']
    list_filter = ["category", "genre", 'region', 'language']
    list_select_related = ['fond', 'category', 'genre']
    resource_class = InformationAdminResource
    filter_horizontal = ['region']

    def get_mtv(self, obj):
        return "\n".join([child.name for child in obj.mtv.all()])

    def get_region(self, obj):
        return "\n".join([child.name for child in obj.region.all()])

    def get_formats(self, obj):
        return '\n'.join([p.name for p in obj.formats.all()])


admin.site.register(Cadre)

admin.site.index_title = "E-Catalog"
admin.site.site_header = 'E-Catalog Administration'
