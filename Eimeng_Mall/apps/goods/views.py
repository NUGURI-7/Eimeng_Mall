from django.shortcuts import render
from rest_framework.views import APIView

from .models import Goods
from Eimeng_Mall.utils import ResponseMessage
from .serializers import GoodsSerializer


# Create your views here.

class GoodsCategoryApiView(APIView):
    def get(self, request, category_id, page):
        start_index = (page-1)*20
        end_index = page*20
        category_data = Goods.objects.filter(
            type_id = category_id).all()[start_index:end_index]
        result_list = []
        for m in category_data:
            result_list.append(m.__str__())

        return ResponseMessage.GoodsResponse.success(result_list)

class GoodsDetailView(APIView):
    def get(self, request, sku_id):

       good_data=Goods.objects.filter(sku_id=sku_id).first()
       #进行序列化, 序列化参数时instance ，反序列化参数时data
       result = GoodsSerializer(instance=good_data)
       print(result)
       return ResponseMessage.GoodsResponse.success(result.data)



