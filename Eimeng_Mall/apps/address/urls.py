

from django.urls import path, include, re_path
from .views import AddressGenericAPIView, AddressGenericListAPIView

urlpatterns = [
    path('index', AddressGenericAPIView.as_view()),
    path('index/list', AddressGenericListAPIView.as_view()),
    re_path("(?P<pk>.*)",AddressGenericAPIView.as_view())
]