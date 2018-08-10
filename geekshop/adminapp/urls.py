from django.urls import path

import adminapp.views as view

app_name = 'admin'

urlpatterns = [
    path('users/create/', view.user_create, name='user_create'),
    path('users/read/', view.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', view.user_update, name='user_update'),
    path('users/delete/<int:pk>/', view.user_delete, name='user_delete'),

    path('categories/create/', view.category_create, name='categories_create'),
    path('categories/read/', view.categories, name='categories'),
    path('categories/update/<int:pk>/', view.category_update, name='categories_update'),
    path('categories/delete/<int:pk>/', view.category_delete, name='categories_update'),

    path('product/create/category/<int:pk>/', view.product_create, name='product_create'),
    path('product/read/category/<int:pk>/', view.products, name='products'),
    path('product/read/<int:pk>/', view.product_read, name='product_read'),
    path('product/update/<int:pk>/', view.product_update, name='product_update'),
    path('product/delete/<int:pk>/', view.product_delete, name='product_delete')
]
