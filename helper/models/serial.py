from django.db import models


class Serial(models.Model):
    video = models.ForeignKey('main.Information', on_delete=models.CASCADE, related_name='seraial')
    part = models.PositiveSmallIntegerField(null=True, blank=True)
    duration = models.TimeField()

    def __str__(self):
        return self.video.name
