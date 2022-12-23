from .models import Patient
from rest_framework.serializers import ModelSerializer

class PatientSerializers(ModelSerializer):
    class Meta:
        model=Patient
        fields = '__all__'