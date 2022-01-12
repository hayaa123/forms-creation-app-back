from django.db.models.query import QuerySet
from django.shortcuts import render
from .serializer import FormShapeSeriaizer
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from .models import FormShape
# Create your views here.

class ListCreateFormShape(ListCreateAPIView):
    serializer_class =FormShapeSeriaizer
    queryset = FormShape.objects.all()

class DeleteUpdateFormitem(RetrieveUpdateDestroyAPIView):
    serializer_class =FormShapeSeriaizer
    queryset = FormShape.objects.all()
