from django.urls import include, path
from Admin import views

urlpatterns = [
    path('', include('Admin.Home.urls')),
    path('', include('Admin.Login.urls')),
    path('users/', include('Admin.Users.urls')),
    path('handbooks/', include('Admin.Handbooks.urls', namespace='handbooks')),
    path('medicine/', include('Admin.Medicine.urls', namespace='medicine')),
    path('clinic-settings/', include('Admin.ClinicSettings.urls', namespace='clinic-settings')),
    path('loggers/', include('Admin.Loggers.urls', namespace='loggers')),
    path('admins/', include('Admin.Admins.urls')),
    path('profile/', include('Admin.Profile.urls')),

    path('api/', include('Admin.Api.urls')),
    path('', include('urls')),
]

handler401 = views.error_401
handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500
