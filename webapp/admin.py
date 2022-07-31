from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birth_date',]
    list_filter = ['gender']
    search_fields = ['name']
    fields = ['id', 'name', 'gender', 'birth_date', 'email', 'school_class', 'address',]
    readonly_fields = ['id']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'subject',]
    list_filter = ['subject']
    search_fields = ['username']
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'subject', 'phone',]
    readonly_fields = ['id']


@admin.register(models.SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher',]
    list_filter = ['name']
    search_fields = ['name']
    fields = ['id', 'name', 'teacher',]
    readonly_fields = ['id']


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name']
    search_fields = ['name']
    fields = ['id', 'name', ]
    readonly_fields = ['id']