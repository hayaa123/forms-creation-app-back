from rest_framework import serializers
from .models import FormShape
class FormShapeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = FormShape
        fields = "__all__"