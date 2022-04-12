# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:16:52 2022

@author: Windows10
"""

class _ProductivitySystem:
    def __init__(self):
        self._role={
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
            }
    def get_role(self, role_id):
        role_type = self._role.get(role_id)
        if not role_type:
            raise ValueError('Not a valid role_id')
        return role_type()
    
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')

class ManagerRole:
    def work(self, hours):
        return (f'screams and yells for {hours} hours')
    
    
class SecretaryRole:
    def work(self, hours):
        return (f'expends {hours} hours doing office paperwork')
        
class SalesRole:
    def work(self, hours):
        return (f'expends {hours} hours on the phone')
        
class FactoryRole:
    def work(self, hours):
        return (f'manufactures gadgets for {hours} hours.')

_productivity_system = _ProductivitySystem()

def get_role(role_id):
    return _productivity_system.get_role(role_id)

def track(employees, hours):
    _productivity_system.track(employees, hours)
