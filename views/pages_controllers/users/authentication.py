'''
Autor: Simone Lima
'''
from django.shortcuts import render
from views.templates_paths.templates import TemplatesPaths
from django.views import View
from django.utils.translation import gettext_lazy as _
from domain.app.services.user import UserService
from django.http import HttpResponseRedirect
from django.urls import reverse
from domain.utils.web import RequestGenericUtils

def sign_in(request):
    return render(request, TemplatesPaths.USERS.SINGN_IN)

class SignInView(View):
    def get(self,*args, **kwargs):
        if not self.request.user.is_authenticated:
                    lingua = _('lang.english')
                    return render(self.request, TemplatesPaths.USERS.SINGN_IN,context={'lingua':lingua})
        else:
            return HttpResponseRedirect(reverse("dashboard:index"))  
    
    def sign_in(request):
        if UserService(request).auth():
            return HttpResponseRedirect(reverse("dashboard:default"))
        RequestGenericUtils.showSingleErrorMessage(request,"Utilizador ou senha incorecta!")
        return HttpResponseRedirect(reverse("users:sign_in"))

    def log_out(request):
        UserService(request).logout()
        return HttpResponseRedirect(reverse("users:sign_in"))
 