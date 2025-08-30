from django.urls import path, include
from .views import medicine_home_view

app_name = 'medicine'

urlpatterns = [
    path('', medicine_home_view, name='home'),
    path('allergy-type/', include('Admin.Medicine.AllergyType.urls')),
    path('allergy-cause/', include('Admin.Medicine.AllergyCause.urls')),
    path('allergy-reactions/', include('Admin.Medicine.AllergyReaction.urls')),
    path('icd-10/', include('Admin.Medicine.ICD10.urls')),
    path('patient-relations/', include('Admin.Medicine.PatientRelations.urls')),
]
