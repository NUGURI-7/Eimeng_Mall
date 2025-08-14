

from django.urls import path, include
from .views import UserApiView

urlpatterns = [
    path('index', UserApiView.as_view()),
]