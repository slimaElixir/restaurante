from django.contrib import auth
#from domain.utils.web
from domain.app.services.menu import MenuService

class UserService:
    def __init__(self, request):
        self.request = request

    def auth(self):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        if not username or not password:
            return False
        user = auth.authenticate(self.request, username=username, password=password)
        if not user:
            return False
        auth.login(self.request, user)
        menu_list = MenuService().load_menu()
        
        return True

    def logout(self):
        auth.logout(self.request)