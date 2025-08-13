from django.urls import include, path

urlpatterns = [
    path('', include('Admin.Home.urls')),
    path('', include('Admin.Login.urls')),
    path('', include('urls')),
]
