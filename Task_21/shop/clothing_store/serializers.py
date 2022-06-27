from rest_framework import serializers

from .models import Brand, Clothing, Item


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
