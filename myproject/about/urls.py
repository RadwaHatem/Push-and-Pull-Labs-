from django.urls import path
from about.views import aboutFun

urlpatterns = [
    path('', aboutFun, name='aboutus' )
]
