from django.db import models


class Category(models.Model):
    fond = models.ForeignKey('helper.Fond', on_delete=models.CASCADE, related_name='fond')
    name = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
