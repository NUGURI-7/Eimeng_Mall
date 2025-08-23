import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User
from utils.password_encode import get_md5


class UserSerializer(serializers.ModelSerializer):
    #email作为用户名进行登录,做一个唯一性验证
    email = serializers.EmailField(
        required=True, allow_blank= False,
        validators=[UniqueValidator(User.objects.all(), message="用户已存在")]
        )
    password = serializers.CharField()
    birthday = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S",required=False)

    #create 方法会被自动调用，可以对数据做验证或者加工
    def create(self, validated_data):
        print(validated_data)
        validated_data["password"] = get_md5(validated_data["password"])
        validated_data["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = User.objects.create(**validated_data)
        return result

    class Meta:
        model = User
        fields = "__all__"