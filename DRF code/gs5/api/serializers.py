from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) # to make field read-only and cannot be modified in database
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # fields = '__all__'  # to include all fields from the model
        # exclude = ['name']  # to exclude specific fields from the model
        # extra_kwargs = {'name': {'read_only': True}}  # another way to make field read-only
        # read_only_fields = ['name']  # another way to make field read-only