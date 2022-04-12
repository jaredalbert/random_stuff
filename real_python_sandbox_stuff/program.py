# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:30:34 2022

@author: Windows10
"""
import json

from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees_new import employee_database, Employee

def print_dict(d):
    print(json.dumps(d, indent=2))

employees = employee_database.employees()

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)



track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())










# from hr import PayRollSystem, HourlyPolicy
# from productivity import ProductivitySystem
# from employees_new import EmployeeDatabase
# import json
# from representations import AsDictionaryMixin

# productivity_system  = ProductivitySystem()
# payroll_system = PayRollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees()

# manager = employees[0]
# manager.payroll = HourlyPolicy(55)


# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

# def print_dict(d):
#     print (json.dumps(d, indent = 2))
    
# for employee in EmployeeDatabase().employees():
#     print_dict(employee.to_dict())






'''import hr
import employees_new
import productivity
import contacts


manager = employees_new.Manager(1, 'John Smith', 1500)
manager.address = contacts.Address('1 Manager Way', 'high hilll', 'CT', '11111')

secretary = employees_new.Secretary(2,"Jane Doe", 4000)
secretary.address = contacts.Address('1 Manager Way', 'high hilll', 'CT', '11111')

factory_worker =  employees_new.FactoryWorker(3,"Jane Doe", 40, 15)
sales_person = employees_new.SalesPerson(4, 'Kevin Bacon', 1000, 250)
temporary_secretary = employees_new.TemporarySecretary(5,"Jane Doed", 40, 90)

employees = [manager, 
             factory_worker, 
             sales_person, 
             secretary, 
             temporary_secretary]
#employees=[salary_employee, hourly_employee, commission_employee]

productivity = productivity.ProductivitySystem()
productivity.track(employees, 40)


payroll = hr.PayRollSystem()
payroll.calculate_payroll(employees)
'''