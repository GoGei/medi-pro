from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country-list'),
    path('<int:country_id>/view/', views.country_view, name='country-view'),
    path('<int:country_id>/edit/', views.country_edit, name='country-edit'),
    path('<int:country_id>/archive/', views.country_archive, name='country-archive'),
    path('<int:country_id>/restore/', views.country_restore, name='country-restore'),

    path('import/', views.country_import, name='country-import'),
    path('export/json/', views.country_export_json, name='country-export-json'),
    path('export/csv/', views.country_export_csv, name='country-export-csv'),
    path('sync/', views.country_sync, name='country-sync'),
    path('sync/external-api/', views.country_sync_external_api, name='country-sync-external-api'),
]
