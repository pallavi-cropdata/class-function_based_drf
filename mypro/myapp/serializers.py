from . models import Student
from rest_framework import serializers

class studentseri(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"