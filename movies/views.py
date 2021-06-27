from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Genre, Movie
from .permissions import IsAdminOrReadOnly
from .serializers import GenreSerializer, MovieSerializer


class MovieFilter(FilterSet):

    class Meta:
        model = Movie
        fields = {
            'name': ['icontains'],
            'director': ['icontains'],
            'genres__name': ['icontains'],
            'imdb_score': ['lte', 'gte'],
            'popularity': ['lte', 'gte'],
        }


class GenreListAPIView(ListCreateAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class GenreDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class MovieListAPIView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    # filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
