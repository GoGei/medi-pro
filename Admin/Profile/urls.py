from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile-view'),
    path('edit/', views.profile_edit, name='profile-edit'),
    path('change-password/', views.profile_change_password, name='profile-change-password'),
]
