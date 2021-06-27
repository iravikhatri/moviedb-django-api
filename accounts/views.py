from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]