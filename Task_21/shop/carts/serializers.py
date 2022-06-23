from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'
