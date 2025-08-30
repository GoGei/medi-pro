from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.icd10_list, name='icd10-list'),
    path('<int:icd10_id>/view/', views.icd10_view, name='icd10-view'),

    path('sync/', views.icd10_sync, name='icd10-sync'),
    path('export/json/', views.icd10_export, name='icd10-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.icd10_export, name='icd10-export-csv', kwargs={'mode': ExportModes.CSV}),
]
