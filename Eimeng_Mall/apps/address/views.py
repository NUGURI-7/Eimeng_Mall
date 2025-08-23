from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.request import Request

from apps.address.models import UserAddress
from apps.address.serializers import AddressSerializer
from utils.jwt_auth import JwtQueryParamAuthorization, JwtAuthorization


# Create your views here.
class AddressGenericAPIView(GenericAPIView, CreateModelMixin,
                            RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer
    authentication_classes = [JwtAuthorization]

    def post(self, request: Request):
        return self.create(request)

    def get(self, request: Request, pk):
        if not request.user.get('status'):
            return JsonResponse(request.user, safe=False)
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.delete(request, pk)


class AddressGenericListAPIView(GenericAPIView, ListModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer
    authentication_classes = [JwtQueryParamAuthorization]

    def get(self, request: Request):
        # 拿到token验证返回的第一个值
        print(request.user)
        # 拿到token返回的第二个值
        print(request.auth)
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)

        return self.list(request)


