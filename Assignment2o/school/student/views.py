from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import Student_list_serializer
from .models import Student_list
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])

def show_student_list(request,id=None):
    if request.method == 'GET':
        student_list =Student_list.objects.all()
        student_serializer =  Student_list_serializer(student_list,many = True)
        return Response(student_serializer.data)

    
    if request.method =='POST':
        data = JSONParser().parse(request)
        students = Student_list.objects.get(id = data['id'])
        student_serializer = Student_list_serializer(data=data)

        if student_serializer.is_valid():
            student_serializer.save()
        else:
             return Response({"message":"data invalid - was not inserted"})
        return Response({"message":"data Updated"})

    
    if request.method =='PUT':
        students = Student_list.objects.get(id=id)
        data = JSONParser().parse(request)
        student_serializer = Student_list_serializer(students,data=data)

        if student_serializer.is_valid():
            student_serializer.save()
        else:
             return Response({"message":"data invalid - was not inserted"})
        return Response({"message":"data Updated"})

    if request.method =="DELETE":
        students =Student_list.objects.get(id = id)
        students.delete()
        return Response({"message":"data Deleted"})