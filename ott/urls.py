from django.urls import path,include
from . import views

urlpatterns = [
    path('movie-list/',views.MovieList.as_view(),name = 'movie-list'),
    path('',views.Home.as_view()),
    path('movie/<int:pk>/',views.MovieDetail.as_view(),name = 'movie-detail'),
    path('platform-list/',views.PlatformList.as_view(),name = 'platform-list'),
    path('platform/<int:pk>/',views.PlatformDetail.as_view(),name = 'platform-detail'),

]