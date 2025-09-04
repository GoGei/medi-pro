from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.setting_list, name='clinic-pre-settings-list'),
    path('add/', views.setting_add, name='clinic-pre-settings-add'),
    path('<int:setting_id>/view/', views.setting_view, name='clinic-pre-settings-view'),
    path('<int:setting_id>/edit/', views.setting_edit, name='clinic-pre-settings-edit'),
    path('<int:setting_id>/archive/', views.setting_archive, name='clinic-pre-settings-archive'),
    path('<int:setting_id>/restore/', views.setting_restore, name='clinic-pre-settings-restore'),

    path('import/', views.setting_import, name='clinic-pre-settings-import'),
    path('export/json/', views.setting_export_json, name='clinic-pre-settings-export-json'),
    path('export/csv/', views.setting_export_csv, name='clinic-pre-settings-export-csv'),
]
