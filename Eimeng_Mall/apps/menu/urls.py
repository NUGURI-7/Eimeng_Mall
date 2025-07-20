

from django.urls import path, include
from .views import GoodsMainMenu, GoodsSubMenu

urlpatterns = [
    path('index', GoodsMainMenu.as_view()),
    path('submenu', GoodsSubMenu.as_view()),
]