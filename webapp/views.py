from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView
from django.views import View
from . import models, forms


# class RegisterView(CreateView):
#     model = User
#     template_name = 'registration/user_create.html'
#     form_class = TeacherCreationForm
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.get_success_url())
#
#     def get_success_url(self):
#         next_url = self.request.GET.get('next')
#         if not next_url:
#             next_url = self.request.POST.get('next')
#         if not next_url:
#             next_url = reverse('tracker:issue-list')
#         return next_url
#
#
# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = 'user_detail.html'
#     context_object_name = 'user_obj'
#     paginate_related_by = 5
#     paginate_related_orphans = 0
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# class UserChangeView(LoginRequiredMixin, UpdateView):
#     model = get_user_model()
#     form_class = UserChangeForm
#     template_name = "user_change.html"
#     context_object_name = "user_obj"
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#     def get_context_data(self, **kwargs):
#         if 'profile_form' not in kwargs:
#             kwargs['profile_form'] = self.get_profile_form()
#         return super().get_context_data(**kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         profile_form = self.get_profile_form()
#         if form.is_valid() and profile_form.is_valid():
#             return self.form_valid(form, profile_form)
#         else:
#             return self.form_invalid(form, profile_form)
#
#     def form_valid(self, form, profile_form):
#         response = super().form_valid(form)
#         profile_form.save()
#         return response
#
#     def form_invalid(self, form, profile_form):
#         context = self.get_context_data(form=form, profile_form=profile_form)
#         return self.render_to_response(context)
#
#     def get_profile_form(self):
#         form_kwargs = {'instance': self.object.profile}
#         if self.request.method == 'POST':
#             form_kwargs['data'] = self.request.POST
#             form_kwargs['files'] = self.request.FILES
#         return TeacherChangeForm(**form_kwargs)
#
#     def get_success_url(self):
#         return reverse('accounts:detail', kwargs={'pk': self.object.pk})
#

class StudentListView(ListView):
    model = models.Student
    template_name = 'index.html'
    context_object_name = 'students'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return forms.SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'student.html'


class StudentUpdateView(UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'update.html'
    context_object_name = 'student'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.kwargs.get('pk')})


class StudentCreateView(CreateView):
    template_name = 'create.html'
    form_class = forms.StudentForm
    model = models.Student

    def form_valid(self, form):
        student = models.Student()
        for key, value in form.cleaned_data.items():
            setattr(student, key, value)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class StudentDeleteView(DeleteView):
    model = models.Student
    context_object_name = 'student'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class SendEmailView(FormView):
    template_name = 'send_email.html'
    form_class = forms.MailForm

    def form_valid(self, form):
        recipients = models.Student.objects.all().values_list(
            'email',
            flat=True,
        )
        send_mail(
            subject=form.cleaned_data.get('title'),
            message=form.cleaned_data.get('text'),
            recipient_list=recipients,
            from_email='school@gmail.com',
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class RegisterView(CreateView):
    model = models.Teacher
    template_name = 'user_create.html'
    form_class = forms.MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url
