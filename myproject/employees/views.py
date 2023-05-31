from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from employees.models import Employee
from employees.forms import  EmployeeForm
# Create your views here.

def employeesFun(request):
    return render(request, 'employees.html')

def empIdFun(request, id):
    
    return HttpResponse("The ID of your employee is " + id)

def employees_list(request):
    employees = Employee.get_all_employees()
    return render(request, 'employees/list.html', context={"employees":employees})

def employee_delete(request, id):
    student = Employee.get_employee(id)
    student.delete()
    redirect_url = reverse('employees.list')
    return redirect(redirect_url)

def employee_show(request, id):
    employee = Employee.get_employee(id)
    return render(request, 'employees/show.html', context={"employee":employee})

def create_employee(request):
    form  = EmployeeForm()
    if request.method =='GET':
        return render(request, 'employees/create.html', context={"form":form})
    else:
        print(request.POST)
        print(request.FILES)
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        redirect_url = reverse('employees.list')
        return redirect(redirect_url)

def edit_employee(request, id ):
    employee = Employee.get_employee(id)
    if request.method =='GET':
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/edit.html', context={"form":form})
    else:
        print(request.POST)
        print(request.FILES)
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        redirect_url = reverse('employees.show',args=[employee.id])
        return redirect(redirect_url)
