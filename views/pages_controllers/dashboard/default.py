'''
Autor: Simone Lima
'''
from django.shortcuts import render
from views.templates_paths.templates import TemplatesPaths
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from domain.app.services.menu import MenuService

class DashboardView(LoginRequiredMixin,View):
    def get(self,*args, **kwargs):
        menu_list = MenuService().load_menu()

        for menu in menu_list:
            print('MENU: ',menu.__dict__)
        return render(self.request, TemplatesPaths.DASHBOARD.DEFAULT,context={'menu_list':menu_list})
