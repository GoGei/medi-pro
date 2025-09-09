from django.urls import path
from . import views

urlpatterns = [
    path('', views.handbooks_update_list, name='handbooks-update-list'),
]
