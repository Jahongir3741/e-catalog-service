from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from .managers import CustomUserManager, AdminManager, EmployeeManager, LowUserManager


class Trk(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# USER MODELS
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        EMPLOYEE = "EMPLOYEE", "employee"
        LOW_USER = "LOW_USER", "low_user"

    role = models.CharField(max_length=10, choices=Role.choices)
    trk = models.OneToOneField(Trk, on_delete=models.CASCADE, null=True, blank=True)
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['password']

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #         return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Admin(User):

    class Meta:
        proxy = True

    admin = AdminManager()

    def save(self, *args, **kwargs):
        self.type = User.Role.ADMIN
        # self.password = make_password(self.password)
        return super().save(*args, **kwargs)


class Employee(User):

    class Meta:
        proxy = True

    employee = EmployeeManager()

    def save(self, *args, **kwargs):
        # self.type = User.Role.EMPLOYEE
        return super().save(*args, **kwargs)


class LowUser(User):

    class Meta:
        proxy = True

    low_user = LowUserManager()

    def save(self, *args, **kwargs):
        self.type = User.Role.LOW_USER
        # self.password = make_password(self.password)
        return super().save(*args, **kwargs)
