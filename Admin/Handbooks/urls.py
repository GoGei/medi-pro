from django.urls import path, include

app_name = 'handbooks'

urlpatterns = [
    path('timezones/', include('Admin.Handbooks.TimezoneHandbook.urls')),
    path('countries/', include('Admin.Handbooks.Country.urls')),
    path('currencies/', include('Admin.Handbooks.Currency.urls')),
]
