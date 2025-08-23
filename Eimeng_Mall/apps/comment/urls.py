

from django.urls import path, re_path
from .views import CommentGenericAPIView

urlpatterns = [
    path('index', CommentGenericAPIView.as_view({
        "get": "list0",
        "post": "save0",
    })),
    re_path("(?P<pk>.*)", CommentGenericAPIView.as_view({
        "get":"single",
        "post":"edit",
        "delete":"delete0",
    }))
]