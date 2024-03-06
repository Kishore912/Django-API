from django.shortcuts import render, redirect
from .forms import EmployeeForm

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
