from django.db import models


class Fond(models.Model):
    name = models.CharField(max_length=100, unique=True)
    uzmtrk = models.ForeignKey('helper.Uzmtrk', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)
