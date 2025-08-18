from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.timezone_list, name='timezones-list'),
    path('<int:timezone_id>/view/', views.timezone_view, name='timezones-view'),
    path('<int:timezone_id>/edit/', views.timezone_edit, name='timezones-edit'),
    path('<int:timezone_id>/archive/', views.timezone_archive, name='timezones-archive'),
    path('<int:timezone_id>/restore/', views.timezone_restore, name='timezones-restore'),

    path('import/', views.timezone_import, name='timezones-import'),
    path('export/json/', views.timezone_export, name='timezones-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.timezone_export, name='timezones-export-csv', kwargs={'mode': ExportModes.CSV}),
    path('sync/', views.timezone_sync, name='timezones-sync'),
]
