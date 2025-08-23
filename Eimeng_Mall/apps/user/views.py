from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializers import UserSerializer
from utils import ResponseMessage
from utils.jwt_auth import create_token
from utils.password_encode import get_md5


# Create your views here.
class UserApiView(APIView):
    # 用户注册
    def post(self, request: Request):

        user_data_serializer = UserSerializer(data=request.data)
        #user_data_serializer 变成一个序列化器
        user_data_serializer.is_valid(raise_exception=True)
        # user_data = User.objects.create(**user_data_serializer.data)
        user_data = user_data_serializer.save()

        #序列化userdata， 把json返回给前端
        user_json = UserSerializer(instance=user_data).data
        return ResponseMessage.UserResponse.success(user_json)

    def get(self, request: Request):
        email = request.query_params.get('email')
        try:
            user_data = User.objects.filter(email=email).first()
            if not user_data:
                raise ValueError('该用户不存在')
            user_ser = UserSerializer(user_data)
            return ResponseMessage.UserResponse.success(user_ser.data)
        except Exception as e :
            print(e)
            return ResponseMessage.UserResponse.failed('用户信息获取失败')

class LoginView(GenericAPIView):

    def post(self, request: Request):
        user_profile = {}
        request_data = request.data
        email = request_data.get('username')
        user_detail = User.objects.filter(email=email).first()
        if user_detail is None:
            return ResponseMessage.UserResponse.other("用户名或密码错误")
        else:
            user_ser = UserSerializer(instance=user_detail, many=False)
            # 用户输入的密码
            input_password = request_data.get("password")
            password = get_md5(input_password)
            # 数据库密码
            db_password = user_ser.data.get("password")
            if password != db_password:
                return ResponseMessage.UserResponse.other("用户名或密码错误")
            else:
                token_info = {
                    'username': email
                }
                token_data = create_token(token_info)
                user_profile["token"] = token_data
                user_profile["username"] = user_ser.data.get("name")
                return ResponseMessage.UserResponse.success(user_profile)