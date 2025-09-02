from django.urls import path
from core.Utils.models.exporters import ExportModes
from . import views

urlpatterns = [
    path('', views.currency_list, name='currency-list'),
    path('add/', views.currency_add, name='currency-add'),
    path('<int:currency_id>/view/', views.currency_view, name='currency-view'),
    path('<int:currency_id>/edit/', views.currency_edit, name='currency-edit'),
    path('<int:currency_id>/archive/', views.currency_archive, name='currency-archive'),
    path('<int:currency_id>/restore/', views.currency_restore, name='currency-restore'),

    path('import/', views.currency_import, name='currency-import'),
    path('export/json/', views.currency_export, name='currency-export-json', kwargs={'mode': ExportModes.JSON}),
    path('export/csv/', views.currency_export, name='currency-export-csv', kwargs={'mode': ExportModes.CSV}),
    path('sync/', views.currency_sync, name='currency-sync'),
]
