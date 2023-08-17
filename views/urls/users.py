from django.urls import path
from views.pages_controllers.users import (
    
    SignInView
)
app_name = 'users'
urlpatterns = [
    path('', SignInView.as_view(), name='sign_in'),
    path('log_in/', SignInView.sign_in, name='log_in'),
    path('log_out/', SignInView.log_out, name='log_out'),
]
