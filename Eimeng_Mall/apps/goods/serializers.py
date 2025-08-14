from rest_framework import serializers

from .models import Goods
from nuguri_mall.settings import IMAGE_URL


class GoodsSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:S")

    def get_image(self, obj):
        new_image_path = IMAGE_URL + obj.image
        return new_image_path

    class Meta:
        model = Goods
        fields = '__all__'