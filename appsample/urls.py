# appname/urls.py
from django.urls import path
from .views import ItemListCreateView , execute_raw_sql

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='auth_permission'),
    path('api/', execute_raw_sql, name='execute_raw_sql'),
]
