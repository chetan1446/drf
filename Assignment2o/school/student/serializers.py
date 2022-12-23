from .models import Student_list
from rest_framework.serializers import ModelSerializer


class Student_list_serializer(ModelSerializer):
    class Meta:
        model = Student_list
        fields = '__all__'