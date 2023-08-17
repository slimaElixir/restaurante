from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel,TreeForeignKey
from domain.utils.db.models import NamedModel, SortableModel
from domain.utils.check_value_utils import CheckValuesUtils
from domain.utils.file_utils import CSVColumnsName, CSV_EXTENSION
from domain.app.models.queries_set.menu import MenuQuerySet, MenuItemQuerySet


class MenuModel(NamedModel, SortableModel):
    app_name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    objects:MenuQuerySet = MenuQuerySet.as_manager()

    class Factory:
        @classmethod
        def instance(cls, name, app_name, icon, position):
            CheckValuesUtils.non_empties([name, app_name, icon, position])
            return MenuModel(name=name, app_name=app_name,icon=icon, sort_order=position)
        
        @classmethod
        def from_dict(cls,row):
            return cls.instance(
                name= row[CSVColumnsName.NAME.value], 
                app_name= row[CSVColumnsName.APP.value],
                icon= row[CSVColumnsName.ICON.value], 
                position=row[CSVColumnsName.POSITION.value]
            )

class MenuItemModel(NamedModel, MPTTModel, SortableModel):
    menu = models.ForeignKey(MenuModel, related_name="items", on_delete=models.CASCADE)
    url_name = models.CharField(max_length=100,null=True,blank=True)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    objects:MenuItemQuerySet = MenuItemQuerySet.as_manager()
    tree = TreeManager()  # type: ignore[django-manager-missing]   

    class Factory:
        @classmethod
        def instance(cls, name, url_name, position):
            CheckValuesUtils.non_empties([name, position])
            return MenuItemModel(name=name, url_name=url_name,sort_order=position)
        
        @classmethod
        def from_dict(cls,row):
            return cls.instance(
                name= row[CSVColumnsName.NAME.value], 
                url_name= row[CSVColumnsName.URL.value],
                position=row[CSVColumnsName.POSITION.value]
            )


    def get_link(self):
        if self.url_name:
            return "{% url '{}:{}' %}".format(self.menu.app_name, self.url_name)
        return None
    
    @property
    def get_link_property(self):
        return  self.get_link()


