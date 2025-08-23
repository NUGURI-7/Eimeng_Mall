

from django.urls import path, include
from .views import UserApiView, LoginView

urlpatterns = [
    path('index', UserApiView.as_view()),
    path('login', LoginView.as_view()),
]