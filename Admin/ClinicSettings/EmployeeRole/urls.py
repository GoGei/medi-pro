from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='employee-role-list'),
    path('<int:role_id>/view/', views.role_view, name='employee-role-view'),
    path('<int:role_id>/edit/', views.role_edit, name='employee-role-edit'),
]
