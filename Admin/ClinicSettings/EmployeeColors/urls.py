from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.color_list, name='employee-color-list'),
    path('add/', views.color_add, name='employee-color-add'),
    path('<int:color_id>/view/', views.color_view, name='employee-color-view'),
    path('<int:color_id>/edit/', views.color_edit, name='employee-color-edit'),
    path('<int:color_id>/archive/', views.color_archive, name='employee-color-archive'),
    path('<int:color_id>/restore/', views.color_restore, name='employee-color-restore'),
    path('<int:color_id>/set-default/', views.color_set_default, name='employee-color-set-default'),

    path('import/', views.color_import, name='employee-color-import'),
    path('export/json/', views.color_export, name='employee-color-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.color_export, name='employee-color-export-csv', kwargs={'mode': ExportModes.CSV}),
    path('sync/', views.color_sync, name='employee-color-sync'),
]
