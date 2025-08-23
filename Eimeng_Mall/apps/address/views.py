from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.request import Request

from apps.address.models import UserAddress
from apps.address.serializers import AddressSerializer


# Create your views here.
class AddressGenericAPIView(GenericAPIView, CreateModelMixin,
                            RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer


    def post(self, request: Request):
        return self.create(request)

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.delete(request, pk)


class AddressGenericListAPIView(GenericAPIView, ListModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer

    def get(self, request: Request):
        return self.list(request)