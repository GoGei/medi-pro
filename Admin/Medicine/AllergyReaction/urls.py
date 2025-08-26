from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.allergy_reaction_list, name='allergy-reactions-list'),
    path('<int:allergy_reaction_id>/view/', views.allergy_reaction_view, name='allergy-reactions-view'),

    path('export/json/', views.allergy_reaction_export, name='allergy-reactions-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.allergy_reaction_export, name='allergy-reactions-export-csv', kwargs={'mode': ExportModes.CSV}),
]
