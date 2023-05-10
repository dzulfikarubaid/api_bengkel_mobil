from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('', views.index),
    path('auth/login/', views.login_api, name='login'),
    path('auth/users/',views.user_list, name='user_list'),
    path('auth/register/',views.register_api, name='register'),
    path('auth/logout/',knox_views.LogoutView.as_view(), name='knox_logout'),
    path('add_servis/',views.add_servis, name='add_servis'),
    path('servis_list/',views.servis_list, name='servis_list'),
    path('update_servis/<int:pk>', views.update_servis, name='update_servis'),
    path('delete_servis/<int:pk>', views.delete_servis, name='delete_servis'),
]