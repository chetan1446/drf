from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializers
from .models import Patient
# import json
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def show_patients(request,id = None):
    if request.method == 'GET':
        patients = Patient.objects.all()
        patient_serializer = PatientSerializers(patients,many=True)
        return Response(patient_serializer.data)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        patients = Patient.objects.get(id = data['id'])
        patient_serializer = PatientSerializers(data=data)

        if patient_serializer.is_valid():
            patient_serializer.save()
        else:
            return Response({"message":"data invalid"})
        return Response({"message":"data updated"})

    if request.method =='PUT':
        patients = Patient.objects.get(id=id)
        data = JSONParser().parse(request)
        patient_serializer = PatientSerializers(patients, data=data)

        if patient_serializer.is_valid():
            patient_serializer.save()
        else:
            return Response({"message":"data invalid - was not inserted"})
        return Response({"message":"data Updated"})

    if request.method =="DELETE":
        patients =Patient.objects.get(id = id)
        patients.delete()
        return Response({"message":"data Deleted"})
