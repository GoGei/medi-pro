from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.allergy_type_list, name='allergy-types-list'),
    path('<int:allergy_type_id>/view/', views.allergy_type_view, name='allergy-types-view'),

    path('sync/', views.allergy_type_sync, name='allergy-types-sync'),
    path('export/json/', views.allergy_type_export, name='allergy-types-export-json',
         kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.allergy_type_export, name='allergy-types-export-csv', kwargs={'mode': ExportModes.CSV}),
]
