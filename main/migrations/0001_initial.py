# Generated by Django 5.0.3 on 2024-05-16 15:30

import django.core.validators
import django.db.models.deletion
import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.utils.poster_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('mtv_index', models.CharField(max_length=100)),
                ('location_on_server', models.CharField(max_length=250)),
                ('color', models.CharField(choices=[('coloured', 'Coloured'), ('write_black', 'Write Black')], default='coloured', max_length=12)),
                ('material', models.CharField(choices=[('ether', 'Ether'), ('primary', 'Primary')], default='primary', max_length=10)),
                ('duration', models.TimeField()),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1920, message="Yilni tug'ri kiriting?"), django.core.validators.MaxValueValidator(2024, message="Yilni tug'ri kiriting?")])),
                ('month', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1, message="Oyni tug'ri kiriting?"), django.core.validators.MaxValueValidator(12, message="Oyni tug'ri kiriting?")])),
                ('day', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1, message="Kunni tug'ri kiriting?"), django.core.validators.MaxValueValidator(31, message="Kunni tug'ri kiriting?")])),
                ('restavrat', models.BooleanField(default=False)),
                ('konfidensial', models.BooleanField(default=False)),
                ('brief_data', models.TextField(blank=True, db_index=True, null=True)),
                ('summary', models.TextField(blank=True, db_index=True, null=True)),
                ('is_serial', models.BooleanField(default=False)),
                ('part', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_categories', to='helper.category')),
                ('fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information_fonds', to='helper.fond')),
                ('formats', models.ManyToManyField(blank=True, null=True, related_name='information_format', to='helper.format')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_genres', to='helper.genre')),
                ('language', models.ManyToManyField(blank=True, null=True, related_name='information_languages', to='helper.language')),
                ('mtv', models.ManyToManyField(blank=True, null=True, related_name='information_mtvs', to='helper.mtv')),
                ('region', models.ManyToManyField(blank=True, null=True, related_name='information_regions', to='helper.region')),
                ('uzmtrk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.uzmtrk')),
                ('poster', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posters', to='main.poster')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.utils.cadre_directory_path)),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='main.information')),
            ],
        ),
    ]
