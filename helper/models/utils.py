from django.db import models


class AbstractClass(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Mtv(AbstractClass):

    objects = models.Manager()

    def __str__(self):
        return self.name


class Region(AbstractClass):

    objects = models.Manager()

    def __str__(self):
        return self.name


class Language(AbstractClass):

    objects = models.Manager()

    def __str__(self):
        return self.name


class Format(AbstractClass):

    objects = models.Manager()

    def __str__(self):
        return self.name
