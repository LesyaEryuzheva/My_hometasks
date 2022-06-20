from rest_framework import serializers
from .models import Clothing


class ClothingDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Clothing
        fields = ('__all__')


class ClothingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothing
        fields = ('name', 'price', 'stock', 'user')
