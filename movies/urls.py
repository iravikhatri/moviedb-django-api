from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreListAPIView.as_view()),
    path('genres/<int:pk>/', views.GenreDetailAPIView.as_view()),
    path('', views.MovieListAPIView.as_view()),
    path('<int:pk>/', views.MovieDetailAPIView.as_view()),
]