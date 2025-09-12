from django.urls import path
from . import views

urlpatterns = [
    path('', views.admins_list, name='admins-list'),
    path('add/', views.admins_add, name='admins-add'),
    path('<int:admins_id>/view/', views.admins_view, name='admins-view'),
    path('<int:admins_id>/edit/', views.admins_edit, name='admins-edit'),
    path('<int:admins_id>/archive/', views.admins_archive, name='admins-archive'),
    path('<int:admins_id>/restore/', views.admins_restore, name='admins-restore'),
    path('<int:admins_id>/set-password/', views.admins_set_password, name='admins-set-password'),
]
