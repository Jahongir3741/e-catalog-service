from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import Information
from helper.models import Fond, Category, Genre, Mtv, Region, Language, Format


class InformationAdminResource(resources.ModelResource):
    fond = fields.Field(column_name='fond', attribute='fond', widget=ForeignKeyWidget(Fond, field='name'))
    category = fields.Field(column_name='category', attribute='category',
                            widget=ForeignKeyWidget(Category, field='name'))
    genre = fields.Field(column_name='genre', attribute='genre', widget=ForeignKeyWidget(Genre, field='name'))
    mtv = fields.Field(column_name='mtv', attribute='mtv', widget=ManyToManyWidget(Mtv, field='name'))
    region = fields.Field(column_name='region', attribute='region', widget=ManyToManyWidget(Region, field='name'))
    language = fields.Field(column_name='language', attribute='language',
                            widget=ManyToManyWidget(Language, field='name'))
    formats = fields.Field(column_name='format', attribute='formats', widget=ManyToManyWidget(Format, field='name'))

    def before_import_row(self, row, **kwargs):
        # fond_name = row["fond"]
        # category_name = row["category"] if row["category"] is not None else None
        # genre_name = row["genre"]
        mtv_name = str(row["mtv"])
        region_name = str(row["region"]).strip()
        language_name = str(row["language"]).strip()
        format_name = str(row["format"]).strip()
        mtv = ''

        if "," in mtv_name:
            mtv_list = mtv_name.split(',')
            for item in mtv_list:
                Mtv.objects.get(name=item)
        elif mtv is None:
            pass
        else:
            Mtv.objects.get(name=mtv_name)

        if "," in region_name:
            region_list = region_name.split(',')
            for item in region_list:
                Region.objects.get(name=item)
            # for item in range(len(region_name)-1):
            #     if region_name[item] == ',':
            #         Region.objects.get(name=region)
            #         region = ''
            #     if count == len(region_name)-1:
            #         Region.objects.get(name=region)
            #         region = ''
            #     region += region_name[item]
            #     count +=1
        elif region_name is None:
            pass
        else:
            Region.objects.get(name=region_name)

        if ',' in language_name:
            lst = language_name.split(',')
            for item in lst:
                Language.objects.get(name=item)
        elif language_name is None:
            pass
        else:
            Language.objects.get(name=language_name)

        if ',' in format_name:
            format_list = format_name.split(',')
            for item in format_list:
                Format.objects.get(name=item)
        elif format_name is None:
            pass
        else:
            Format.objects.get(name=format_name)

    class Meta:
        model = Information
