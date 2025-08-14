from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.request import Request

from apps.address.models import UserAddress
from apps.address.serializers import AddressSerializer


# Create your views here.
class AddressGenericAPIView(GenericAPIView, CreateModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer


    def post(self, request: Request):
        return self.create(request)
