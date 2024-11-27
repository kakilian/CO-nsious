from rest_framework import serializers
from .models import EmployeeProfile

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ['id', 'employee', 'total_points']