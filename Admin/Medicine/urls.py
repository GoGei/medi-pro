from django.urls import path, include

app_name = 'medicine'

urlpatterns = [
    path('allergy-type/', include('Admin.Medicine.AllergyType.urls')),
]
