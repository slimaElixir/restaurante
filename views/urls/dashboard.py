from django.urls import path
from views.pages_controllers.dashboard import (
    DashboardView
)
app_name = 'dashboard'
urlpatterns = [
    path('', DashboardView.as_view(), name='default'),
]
