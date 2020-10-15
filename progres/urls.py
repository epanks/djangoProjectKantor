from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_balai', views.list_balai, name='list_balai'),
]
