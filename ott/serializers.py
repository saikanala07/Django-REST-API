from rest_framework import serializers
from .models import Movie,MoviePlatform



class MoviePlatformSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = MoviePlatform
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    ott_name = serializers.CharField(source= 'ott_name',read_only= True)
    class Meta:
        model = Movie
        fields = ['name','description','active','ott_name']
        


        

