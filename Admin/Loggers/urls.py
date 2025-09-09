from django.urls import path, include

app_name = 'loggers'

urlpatterns = [
    path('handbook-updates/', include('Admin.Loggers.HandbookUpdateLog.urls')),
]
