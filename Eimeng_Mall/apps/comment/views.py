from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.request import Request
from rest_framework.viewsets import ViewSetMixin

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


# Create your views here.
class CommentGenericAPIView(ViewSetMixin,GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                            UpdateModelMixin, DestroyModelMixin,

                            ):
    queryset = Comment.objects
    serializer_class = CommentSerializer

    def single(self, request: Request, pk):
        return self.retrieve(request, pk)

    def list0(self, request: Request):
        return self.list(request)

    def edit(self, request: Request, pk):
        return self.update(request, pk)

    def save0(self, request: Request):
        return self.create(request)

    def delete0(self, request: Request, pk):
        return self.destroy(request, pk)