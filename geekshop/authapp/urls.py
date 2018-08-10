from django.urls import path

import authapp.views as views

app_name = 'auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]