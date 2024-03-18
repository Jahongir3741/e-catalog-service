from django.utils import timezone

now = timezone.now()


def image_directory_path(instance, filename):
    return f"{instance}/{now.year}/{now.month}/{now.day}/{filename}"
