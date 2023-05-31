from django.urls import path
from contact.views import contactFun

urlpatterns = [
    path('', contactFun, name='contactus' )
]