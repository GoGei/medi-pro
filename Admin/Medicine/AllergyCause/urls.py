from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.allergy_cause_list, name='allergy-causes-list'),
    path('<int:allergy_cause_id>/view/', views.allergy_cause_view, name='allergy-causes-view'),

    path('export/json/', views.allergy_cause_export, name='allergy-causes-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.allergy_cause_export, name='allergy-causes-export-csv', kwargs={'mode': ExportModes.CSV}),
]
