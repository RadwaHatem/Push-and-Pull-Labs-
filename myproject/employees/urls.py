from django.urls import path
from employees.views import employee_delete, employee_show, edit_employee, create_employee, employees_list, employeesFun

urlpatterns = [
    path('', employeesFun, name='employees' ),
    path('list', employees_list, name='employees.list'),
    path('list/<int:id>/delete', employee_delete, name='employees.delete'),
    path('list/<int:id>', employee_show, name='employees.show'),
    path('create', create_employee, name='employees.create'),
    path('list/<int:id>/edit', edit_employee, name='employees.edit'),
]

