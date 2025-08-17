from django.urls import include, path
from Admin import views

urlpatterns = [
    path('', include('Admin.Home.urls')),
    path('', include('Admin.Login.urls')),
    path('users/', include('Admin.Users.urls')),
    path('', include('urls')),
]

handler401 = views.error_401
handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500
