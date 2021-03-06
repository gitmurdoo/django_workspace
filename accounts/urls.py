from django.urls import path
from . import views

urlpatterns = [
    # /accounts/login/ => settings.LOGIN_URL
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('password_change', views.password_change, name='password_change'),
]
