from django.urls import path
from .views import EmployeeView,SuccessView ,kishore

urlpatterns = [
    
    path('add/',EmployeeView,name='add'),
    path('Success/',SuccessView,name='Success_url'),
    # path('display/',EmployeeSerializerView,name='gg')
    path('employee/',kishore.as_view(),name='kishore'),
    path('employee/<int:emp_id>',kishore.as_view(),name='kishore2')
]