from django.urls import path, include

app_name = 'clinic-settings'

urlpatterns = [
    path('employee-colors/', include('Admin.ClinicSettings.EmployeeColors.urls')),
]
