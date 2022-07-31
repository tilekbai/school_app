from django.urls import path

from . import views


urlpatterns = [
    path('', views.StudentListView.as_view(), name="index"),
    path('<int:pk>/student', views.StudentDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.StudentUpdateView.as_view(), name='update'),
    path('create/', views.StudentCreateView.as_view(), name='create'),
    path('<int:pk>/delete', views.StudentDeleteView.as_view(), name='delete'),
    path('send/', views.SendEmailView.as_view(), name='send_email'),
    path('register/', views.RegisterView.as_view(), name='register'),
]