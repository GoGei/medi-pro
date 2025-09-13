from django.urls import path, include
from . import views

app_name = 'medicine'

urlpatterns = [
    path('', views.medicine_home_view, name='home'),
    path('sync/allergy-cause/', views.allergy_cause_sync, name='home-allergy-causes-sync'),
    path('sync/allergy-reaction/', views.allergy_reaction_sync, name='home-allergy-reactions-sync'),
    path('sync/allergy-type/', views.allergy_type_sync, name='home-allergy-types-sync'),
    path('sync/icd-10/', views.icd10_sync, name='home-icd10-sync'),

    path('allergy-type/', include('Admin.Medicine.AllergyType.urls')),
    path('allergy-cause/', include('Admin.Medicine.AllergyCause.urls')),
    path('allergy-reactions/', include('Admin.Medicine.AllergyReaction.urls')),
    path('icd-10/', include('Admin.Medicine.ICD10.urls')),
    path('patient-relations/', include('Admin.Medicine.PatientRelations.urls')),
]
