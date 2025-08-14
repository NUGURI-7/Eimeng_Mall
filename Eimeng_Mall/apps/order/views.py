from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from apps.order.models import OrderGoods
from apps.order.serializers import OrderGoodsSerializer


# Create your views here.
class OrderGoodsGenericAPIView(GenericAPIView):
    queryset = OrderGoods.objects
    serializer_class = OrderGoodsSerializer

    def post(self, request: Request):
        self.get_queryset()
        # 序列化传进来的对象, data 是字典 ，request.data 拿到{}
        ser_request = self.get_serializer(data=request.data)
        # print(self.get_queryset())
        # print(self.get_serializer())
        ser_request.is_valid(raise_exception=True)
        ser_request.save()
        return JsonResponse("ok", safe=False)

    def get(self, request: Request):
        ok = self.get_serializer(instance=self.get_queryset(), many=True)
        result = ok.data
        print(result)
        return  JsonResponse(result, safe=False)