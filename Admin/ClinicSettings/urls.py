from django.urls import path, include

app_name = 'clinic-settings'

urlpatterns = [
    path('employee-colors/', include('Admin.ClinicSettings.EmployeeColors.urls')),
    path('employee-roles/', include('Admin.ClinicSettings.EmployeeRole.urls')),
    path('clinic-pre-settings/', include('Admin.ClinicSettings.ClinicPreSettings.urls')),
]
