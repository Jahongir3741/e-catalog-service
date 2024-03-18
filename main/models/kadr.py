from django.db import models
from main.utils import image_directory_path


class Cadre(models.Model):
    image = models.ImageField(upload_to=image_directory_path)
    information = models.ForeignKey('main.Information', on_delete=models.CASCADE, related_name='information')

    def __str__(self):
        return f'video_cadre - {self.pk}'
