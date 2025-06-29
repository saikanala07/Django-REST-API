# Create your views here.
from django.shortcuts import render 
from django.http import Http404 

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 

from .models import Movie,MoviePlatform
from .serializers import MovieSerializer,MoviePlatformSerilaizer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Home(APIView):
    
    def get(self,request):
        content = {'msg' : 'Hello Welcome to my API Home Page!'}
        return Response(content)
    
class MovieList(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True) 
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
							status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class MovieDetail(APIView): 
    # authentication_classes = [BasicAuthentication]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        movie= self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    
    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 



class PlatformList(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        movieplatforms = MoviePlatform.objects.all()
        serializer = MoviePlatformSerilaizer(movieplatforms, many=True) 
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MoviePlatformSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
							status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class PlatformDetail(APIView): 
    # authentication_classes = [BasicAuthentication]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return MoviePlatform.objects.get(pk=pk)
        except MoviePlatform.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        movie_platform = self.get_object(pk)
        serializer = MoviePlatformSerilaizer(movie_platform)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        movie_platform= self.get_object(pk)
        serializer = MoviePlatformSerilaizer(movie_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    
    def delete(self, request, pk, format=None):
        movie_platform = self.get_object(pk)
        movie_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
