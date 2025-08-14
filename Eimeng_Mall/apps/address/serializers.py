from rest_framework import serializers

from apps.address.models import UserAddress


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = "__all__"