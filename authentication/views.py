from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serialazers import RegisterSerializer, MyTokenObtainPairSerializer, UserListSerializer
from rest_framework import generics
from .models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = UserListSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
