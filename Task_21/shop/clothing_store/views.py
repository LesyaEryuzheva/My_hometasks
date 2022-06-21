from rest_framework import generics, response, status, decorators
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

    @decorators.action(
        detail=True,
        methods=['post'],
        url_path='add-to-cart',
    )
    def add_item_to_cart(self, request, pk=None):
        item = self.get_object()
        cart = request.user.cart
        cart.clothing.add(item)
        return response.Response(status=status.HTTP_200_OK)

    def delete_item_to_cart(self, request, pk=None):
        item = self.get_object()
        cart = request.user.cart
        cart.clothing.delete(item)
        return response.Response(status=status.HTTP_200_OK)


class ClothingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingDetailSerializer
