from django.urls import path
from . import views

urlpatterns = [
    path('', views.timezone_list, name='timezones-list'),
    path('<int:timezone_id>/view/', views.timezone_view, name='timezones-view'),
    path('<int:timezone_id>/edit/', views.timezone_edit, name='timezones-edit'),
    path('<int:timezone_id>/archive/', views.timezone_archive, name='timezones-archive'),
    path('<int:timezone_id>/restore/', views.timezone_restore, name='timezones-restore'),

    # path('<int:timezone_id>/export/', views.timezone_restore, name='timezones-restore'),
]
