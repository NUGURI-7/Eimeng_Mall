from rest_framework import serializers

from apps.order.models import OrderGoods


class OrderGoodsSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderGoods
        fields = "__all__"