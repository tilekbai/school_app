from django.contrib.auth.models import AbstractUser
from django.db import models
from . import constants



class Student(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Full Name'
    )
    email = models.EmailField(
        max_length=254,
    )
    birth_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
    )
    school_class = models.ForeignKey(
        verbose_name='School Class',
        to='SchoolClass',
        on_delete=models.CASCADE,
        related_name='students',
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Address',
    )
    gender = models.CharField(
        verbose_name='Gender',
        max_length=6,
        choices=constants.GenderVariants.CHOICES,
        null=True,
        blank=True,
    )


class SchoolClass(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    teacher = models.ForeignKey(
        verbose_name='Teacher',
        to='Teacher',
        on_delete=models.CASCADE,
        related_name='classes',
        blank=True,
        null=True,
    )
    school = models.ForeignKey(
        verbose_name='School',
        to='School',
        on_delete=models.CASCADE,
        related_name='classes',
        blank=True,
        null=True,
    )


class School(models.Model):
    name = models.CharField(
        verbose_name='School name',
        max_length=255,
        null=True,
        blank=True,
    )


class Teacher(AbstractUser):
    phone = models.CharField(
        max_length=15,
        unique=True,
    )
    subject = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Subject',
    )
    # USERNAME_FIELD = 'phone_number'