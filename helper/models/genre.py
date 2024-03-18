from django.db import models


class Genre(models.Model):
    category = models.ForeignKey('helper.Category', on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
