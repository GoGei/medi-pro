from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.patient_relation_list, name='patient-relations-list'),
    path('<int:patient_relation_id>/view/', views.patient_relation_view, name='patient-relations-view'),

    path('export/json/', views.patient_relation_export, name='patient-relations-export-json',
         kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.patient_relation_export, name='patient-relations-export-csv',
         kwargs={'mode': ExportModes.CSV}),
]
