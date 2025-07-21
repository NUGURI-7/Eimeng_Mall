

from django.urls import path
from .views import GoodsCategoryApiView, GoodsDetailView

urlpatterns = [
    path('category/<int:category_id>/<int:page>', GoodsCategoryApiView.as_view()),
    path('detail/<int:sku_id>', GoodsDetailView.as_view()),
]