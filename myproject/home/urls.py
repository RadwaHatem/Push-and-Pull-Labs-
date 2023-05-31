from django.urls import path
from home.views import homeFun

urlpatterns = [
    path('', homeFun, name='home' )
]