

from django.urls import path, include
from .views import OrderGoodsGenericAPIView

urlpatterns = [
    path('index', OrderGoodsGenericAPIView.as_view()),
]