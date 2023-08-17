'''
@autor Simone Lima
'''
import pandas as pd
from .files import AppFilesPath
from domain.app.models import MenuModel, MenuItemModel
from domain.utils.file_utils import JSON_EXTENSION
from django.db import transaction
import json

class MenuService:
    def load(self):
        menu_df = pd.read_csv(AppFilesPath.MENU)
        menus:dict = {}

        for index, row in menu_df.iterrows():
            menu_instance:MenuModel = MenuModel.Factory.from_dict(row=row)
            self.__create_menu_and_items_instances(menu_instance=menu_instance)
            menus[menu_instance.app_name] = (menu_instance)
    
    @transaction.atomic
    def __create_menu_and_items_instances(self, menu_instance:MenuModel, ):
        print('Criando Menu: ',menu_instance.__dict__)
        try:
            old_menu_instance:MenuModel = MenuModel.objects.get_by_name(menu_instance.name)
            old_menu_instance.app_name = menu_instance.app_name
            old_menu_instance.icon = menu_instance.icon
            old_menu_instance.save()
            menu_instance = old_menu_instance
            print('Item: ',old_menu_instance.__dict__)
        except MenuModel.DoesNotExist:
            menu_instance.save()

        items_file = open ('{}{}{}'.format(AppFilesPath.MENU_ITENS,menu_instance.app_name,JSON_EXTENSION), "r")
        items_data = json.loads(items_file.read())
        items_file.close()

        items = []
        #print('items json: ',items_data)
        for item in items_data:
            item_instance:MenuItemModel = MenuItemModel.Factory.from_dict(item)
            print('Criando item: ',item_instance.__dict__)
            try:
                old_item_instance:MenuItemModel = MenuItemModel.objects.get_by_menu_and_name(menu_instance, item_instance.name)
                old_item_instance.name = item_instance.name
                old_item_instance.sort_order = item_instance.sort_order
                old_item_instance.url_name = item_instance.url_name
                old_item_instance.save()
            except MenuItemModel.DoesNotExist:
                item_instance.menu = menu_instance
                old_item_instance.save()

            items.append(MenuItemModel.Factory.from_dict(item))
        
        print('FIM DE CRIACAO DEITEMS')

    def load_menu(self):
        return MenuModel.objects.find_all()
