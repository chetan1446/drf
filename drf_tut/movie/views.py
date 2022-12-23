from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer,UserSerializer
from .models import MovieBank
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
import json
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def show_movies(request,movie_id=None):
    if request.method == "GET":
        movies = MovieBank.objects.all() 
        movie_serializer = MovieSerializer(movies,many=True)
        return Response(movie_serializer.data)
    
    if request.method == "POST":
        data = JSONParser().parse(request)
        movie = MovieBank.objects.get(title=data['title'])
        if movie:
            return Response({"message":"data duplicate - was not inserted"})
            
        movie_serializer = MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
        else:
            return Response({"message":"data invalid - was not inserted"})
        return Response({"message":"data inserted"})
    
    if request.method == "PUT":
        movie = MovieBank.objects.get(movie_id=movie_id) 
        data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(movie,data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
        else:
            return Response({"message":"data invalid - was not inserted"})
        return Response({"message":"data Updated"})

    if request.method == "DELETE":
        try:
            movie = MovieBank.objects.get(movie_id=movie_id)
            movie.delete()
        except:
            return Response({"message":"data not Deleted, no movie id"})
        return Response({"message":"data Deleted"})

def show_movies_old(request):
    final_data = []
    movies = MovieBank.objects.all()
    for movie in movies:
        result = {
            "movie_id":movie.movie_id,
            "title":movie.title,
            "genre":movie.genre,
            "collection":str(movie.collection) + " Million"
        }
        final_data.append(result)
    return HttpResponse(json.dumps(final_data))


class MoviesAPIView(APIView):
    def get(self,request):
        movies = MovieBank.objects.all()
        movie_serializer = MovieSerializer(movies,many=True)
        return Response(movie_serializer.data)

    def post(self,request):
        return Response({"message":"This is a POST request"})

    def put(self,request):
        data = json.loads(request.body)
        movie_id = data.get("movie_id")
        movie = MovieBank.objects.get(movie_id=movie_id)
        movie.title = data.get("title")
        movie.save()
        return Response({"message":"movie updated successfully"})

    def delete(self,request):
        return Response({"message":"This is a DELETE request"})
    
    
class ShowUsersAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShowMoviesAPIView(ListAPIView):
    queryset = MovieBank.objects.all()
    serializer_class = MovieSerializer


    