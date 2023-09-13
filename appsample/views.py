from django.shortcuts import render

# Create your views here.

# appname/views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.db import connection
from django.http import JsonResponse

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(x.capitalize() or '_' for x in parts[1:])


def execute_raw_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM auth_permission")
        columns = [snake_to_camel(col[0]) for col in cursor.description]
        results = [ dict(zip(columns,row)) for row in cursor.fetchall()]
    return JsonResponse({"data": results})

