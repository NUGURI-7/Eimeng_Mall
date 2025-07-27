from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    sku_id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    class Meta:
        model = Cart
        fields = '__all__'