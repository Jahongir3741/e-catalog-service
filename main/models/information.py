from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


class Information(models.Model):
    objects = models.Manager()

    class Color(models.TextChoices):
        COLOURED = 'coloured'
        WRITE_BLACK = 'write_black'

    class Material(models.TextChoices):
        ETHER = 'ether'
        PRIMARY = 'primary'

    name = models.CharField(max_length=300, db_index=True)
    uzmtrk = models.ForeignKey('helper.Uzmtrk', on_delete=models.SET_NULL, null=True, blank=True)
    fond = models.ForeignKey('helper.Fond', on_delete=models.CASCADE, related_name='information_fonds')
    category = models.ForeignKey('helper.Category', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='video_categories')
    genre = models.ForeignKey('helper.Genre', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='video_genres')
    mtv = models.ManyToManyField('helper.Mtv', null=True, blank=True, related_name='information_mtvs')
    region = models.ManyToManyField('helper.Region', related_name='information_regions', null=True, blank=True)
    language = models.ManyToManyField('helper.Language', related_name='information_languages', null=True, blank=True)
    formats = models.ManyToManyField('helper.Format', related_name='information_format', null=True, blank=True)
    poster = models.OneToOneField('main.Poster', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='posters')
    mtv_index = models.CharField(max_length=100)
    location_on_server = models.CharField(max_length=250)
    color = models.CharField(max_length=12, choices=Color.choices, default=Color.COLOURED)
    material = models.CharField(max_length=10, choices=Material.choices, default=Material.PRIMARY)
    duration = models.TimeField()
    year = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1920, message="Yilni tug'ri kiriting?"),
        MaxValueValidator(int(date.today().year), message="Yilni tug'ri kiriting?")
    ])
    month = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1, message="Oyni tug'ri kiriting?"),
        MaxValueValidator(12, message="Oyni tug'ri kiriting?")
    ])
    day = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1, message="Kunni tug'ri kiriting?"),
        MaxValueValidator(31, message="Kunni tug'ri kiriting?")
    ])
    restavrat = models.BooleanField(default=False)
    konfidensial = models.BooleanField(default=False)
    brief_data = models.TextField(null=True, blank=True, db_index=True)
    summary = models.TextField(null=True, blank=True, db_index=True)
    is_serial = models.BooleanField(default=False)
    part = models.PositiveSmallIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def clean(self):
        if not self.is_serial:
            if self.part is not None:
                raise ValidationError("Qism qushish mumkin emas")
        return self

    def __str__(self):
        return self.name
