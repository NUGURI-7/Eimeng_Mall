

from django.urls import path, include
from .views import AddressGenericAPIView

urlpatterns = [
    path('index', AddressGenericAPIView.as_view()),
]