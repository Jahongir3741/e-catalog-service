from django.db import models
from random import randint
from .utils import file_directory_path
from django.core.validators import FileExtensionValidator


class Letter(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(default=randint(10000, 99999))
    file = models.FileField(upload_to=file_directory_path, validators=[FileExtensionValidator(['pdf', 'docs'])])
    user = models.ForeignKey('authentication.LowUser', on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='letters')
    is_active = models.BooleanField(default=True)
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.name
