from django.db import models
from main.utils import cadre_directory_path


class Cadre(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to=cadre_directory_path)
    information = models.ForeignKey('main.Information', on_delete=models.CASCADE, related_name='information')

    def __str__(self):
        return f'video_cadre - {self.pk}'
