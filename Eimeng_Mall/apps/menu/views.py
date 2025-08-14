from django.http import HttpResponse
from django.views import View

from .models import MainMenu, SubMenu
from utils import ResponseMessage


# Create your views here.
class GoodsMainMenu(View):
    def get(self, request):
        print('get is coming')
        main_menu = MainMenu.objects.all()
        result_list = []
        for m in main_menu:
            result_list.append(m.__str__())

        return ResponseMessage.MenuResponse.success(result_list)

    def post(self, request):
        print('post is coming')
        return HttpResponse('post is coming')

class GoodsSubMenu(View):
    def get(self, request):
        main_menu_id = request.GET.get('main_menu_id')
        sub_menu = SubMenu.objects.filter(main_menu_id=main_menu_id)
        result_list = []
        for m in sub_menu:
            result_list.append(m.__str__())
        return ResponseMessage.MenuResponse.success(result_list)


