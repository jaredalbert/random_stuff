# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:10:20 2022

@author: Windows10
"""
'''from hr import (HourlyPolicy, SalaryPolicy, CommissionPolicy)
from productivity import (ManagerRole, SecretaryRole, SalesRole, 
FactoryRole)'''

from productivity import get_role #ProductivitySystem
from hr import get_policy #PayRollSystem
from contacts import get_employee_address #AddressBook
from representations import AsDictionaryMixin

class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
             'name': 'Mary Poppins',
             'role': 'manager'             
             },
            2:{
             'name':'John Smith',
             'role':'secretary'
             },
            3:{
             'name':'Kevin Bacon',
             'role':'sales'},
            4:{
             'name':'Jane Doe',
             'role':'factory'
             },
            5:{
             'name':'Robin Williams',
             'role':'secretary'}
                  }
        # self.productivity = ProductivitySystem()
        # self.payroll = PayRollSystem()
        # self.employee_address = AddressBook()
    
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]
        #return [self._create_employee(**data) for data in self._employees]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalide employee_id')
        return info
    
    # def _create_employee(self, id, name, role):
    #     address = self.employee_address.get_employee_address(id)
    #     employee_role=self.productivity.get_role(role)
    #     payroll_policy = self.payroll.get_policy(id)
    #     return Employee(id, name, address, employee_role, payroll_policy)
class Employee(AsDictionaryMixin):
    def __init__(self, id):
       self.id = id
       info = employee_database.get_employee_info(self.id)
       self.name = info.get('name')
       self._role = get_role(info.get('role'))
       self.address = get_employee_address(self.id)
       self._payroll = get_policy(self.id)
# class Employee(AsDictionaryMixin):
#     def __init__(self, id, name, address, role, payroll):
#         self.id = id
#         self.name = name
#         self.address = address
#         self._role = role
#         self._payroll = payroll
    
    
    def work(self, hours):
        duties = self._role.work(hours)
        print(f'Employee {self.id} = {self.name}')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)
    
    def calculate_payroll(self):
        return self._payroll.calculate_payroll()
    
    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll= new_policy

employee_database = _EmployeeDatabase()
'''
class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)
    
class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)
        
class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)'''
