# appname/urls.py
from django.urls import path
from .views import ItemListCreateView , execute_raw_sql , get_item_list

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='auth_permission'),
    path('api/', execute_raw_sql, name='execute_raw_sql'),
    path('api/items', get_item_list, name='get_item_list'),
]
