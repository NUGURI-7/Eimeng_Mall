from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import Request

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
                is_delete=0,
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
            return HttpResponse('更新成功！')
        else:
            # 库中没有对应的已经存在的数据时插入新数据

            cart_add = CartSerializer(data=request_data)
            cart_add.is_valid(raise_exception=True)
            Cart.objects.create(**cart_add.data)
            return HttpResponse('数据不存在')

    def get(self, request: Request):
        request.data = request_data
        eamil = request_data.get('email')
        result = Cart.objects.filter(email=eamil).all()

        return ResponseMessage.