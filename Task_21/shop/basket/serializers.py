from rest_framework import serializers

from clothing_store.models import Clothing, Category
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ClothingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Clothing
        fields = '__all__'
