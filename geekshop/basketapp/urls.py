from django.urls import path

import basketapp.views as views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='view'),
    path('add/<int:pk>/', views.basket_add, name='add'),
    path('remove/<int:pk>/', views.basket_remove, name='remove')
]