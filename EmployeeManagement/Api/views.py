from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response

def EmployeeView(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Success_url')  # Redirect to the success URL
    else:
        form = EmployeeForm()
    return render(request, 'forms.html', {'form': form})

def SuccessView(request):
    return render(request,'Success.html')



# def EmployeeSerializerView(request):
#     employee = Employee.objects.all()
#     dict1={
#         'data':employee
#     }
#     return render(request,'display.html',dict1)

class kishore(APIView):
    def get(self,request,emp_id=None):
        if emp_id is not None:
            try:
                employee = Employee.objects.get(emp_id=emp_id)
                new_data = EmployeeSerializer(employee)
                return Response(new_data.data)
            except Employee.DoesNotExist:
                return Response({'error':'Employee not found'})
        a=Employee.objects.all()
        b=EmployeeSerializer(a,many=True)
        return Response(b.data)
    
    def post(self,request):
        new_data = EmployeeSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({
                'message' : 'successfully created',
                'data' : new_data.data
            })
        
        return Response(new_data.errors)
    
    def put(self,request,emp_id):
        employee = Employee.objects.get(emp_id=emp_id)
        new_data = EmployeeSerializer(employee,data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({
                'message':'Successfully updated',
                'data':new_data.data
            })
        
        return Response(new_data.errors)
    
    def delete(self,request,emp_id):
        employee = Employee.objects.get(emp_id=emp_id)
        try:
            employee.delete()
            return Response({'message':'Successfully deleted'})
        except Employee.DoesNotExist:
                return Response({'error':'Employee not found'})
