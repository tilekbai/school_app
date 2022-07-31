from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.forms import widgets

from . import models


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ('name', 'email', 'birth_date', 'school_class', 'address', 'gender')


class MailForm(forms.Form):

    title = forms.CharField(max_length=200, required=True, label='Title')
    text = forms.CharField(max_length=3000, required=True, label='Text',widget=widgets.Textarea)


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        if last_name == '' and first_name == '':
            raise forms.ValidationError('Fill Out First Name Field!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if models.Teacher.objects.filter(phone=data).exists():
            raise forms.ValidationError("We have a user with this phone number")
        return data

    class Meta:
        model =models.Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'subject']