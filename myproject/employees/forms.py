from django import forms

""" create form based on the model"""
from employees.models import  Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
