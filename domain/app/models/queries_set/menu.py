from domain.utils.db.manager import NamedQuerySet

class MenuQuerySet(NamedQuerySet):
    pass

class MenuItemQuerySet(NamedQuerySet):
    def get_by_menu_and_name(self, menu,name):
        return self.get(menu=menu, name=name)


