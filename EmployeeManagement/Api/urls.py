from django.urls import path
from .views import EmployeeView,SuccessView

urlpatterns = [
    
    path('add/',EmployeeView,name='add'),
    path('Success/',SuccessView,name='Success_url')
]