from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Clothing
from .serializer import ClothingDetailSerializer, ClothingListSerializer


class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class ClothingListView(generics.ListAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingListSerializer


class ClothingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingDetailSerializer
