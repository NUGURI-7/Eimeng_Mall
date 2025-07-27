

from django.urls import path
from .views import CartView

urlpatterns = [
    path('index', CartView.as_view()),
]