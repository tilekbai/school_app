from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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


@receiver(post_save, sender=Student)
def send_mail_to_subs(sender, instance, created, **kwargs):
    if not created:
        return

    send_mail(
        subject='Account created',
        message=f'Hi, {instance.name}! Your account is created',
        recipient_list=[instance.email,],
        from_email='school@gmail.com',
        fail_silently=False,
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
    USERNAME_FIELD = 'phone'