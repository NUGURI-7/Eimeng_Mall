from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import Request

from utils import ResponseMessage
from .models import Cart
from .serializers import CartSerializer


# Create your views here.
class CartView(APIView):

# todo
    def post(self, request):
        request_data = request.data
        email = request_data.get('email')
        sku_id = request_data.get('sku_id')
        nums = request_data.get('nums')
        is_delete = request_data.get('is_delete')
        is_exist = Cart.objects.filter(
                email=email,
                is_delete=0,
                sku_id=sku_id
        )
        if is_exist.exists():
            existed_data = is_exist.get(
                email=email,
                sku_id=sku_id
            )
            if is_delete == 0:
                new_nums = nums + existed_data.nums
                request_data['nums'] = new_nums
            elif is_delete == 1:
                request_data['nums'] = existed_data.nums
            #反序列化
            cart_result = CartSerializer(data=request_data)
            #数据校验
            cart_result.is_valid(raise_exception=True)
            #更新数据
            Cart.objects.filter(email=email,
                is_delete=0,
                sku_id=sku_id).update(**cart_result.data)
            if is_delete == 0:
                return ResponseMessage.CartResponse.success('更新成功！')
            elif is_delete == 1:
                return ResponseMessage.CartResponse.success('删除成功')
        else:
            if is_delete == 1:
                return ResponseMessage.CartResponse.success('无法删除不存在的记录')
            # 库中没有对应的已经存在的数据时插入新数据
            cart_add = CartSerializer(data=request_data)
            cart_add.is_valid(raise_exception=True)
            Cart.objects.create(**cart_add.data)

            return ResponseMessage.CartResponse.success('插入成功')

    def get(self, request: Request):
        email = request.query_params.get('email')
        result = Cart.objects.filter(email=email, is_delete=0).all()

        return ResponseMessage.CartResponse.success(CartSerializer(instance=result, many=True).data)