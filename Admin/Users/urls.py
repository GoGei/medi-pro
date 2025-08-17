from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='users-list'),
    path('<int:user_id>/view/', views.user_view, name='users-view')
]
