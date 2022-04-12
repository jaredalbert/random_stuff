# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:32:48 2022

@author: Windows10
"""
from representations import AsDictionaryMixin
class _AddressBook:
    def __init__(self):
        self.employee_address = {
            1:Address('222 wdewd', 'teba', 'ny', '10991'),
            2:Address('111', 'fere', 'nj', '10226'),
            3:Address('dasdf we', 'dfds', 'ny', '10992'),
            4:Address('2 dalmation dr', 'margoplois', 'wa' ,'10882'),
            5:Address(' 32 sway rd', 'ascan', 'ma','10882'),
            }
    
    def get_employee_address(self, employee_id):
        address = self.employee_address.get(employee_id)
        if not address:
            raise ValueError('not a valie employee id')
        return (address)




class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2 =''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2
    
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)
        
_address_book = _AddressBook()

def get_employee_address(employee_id):
        return _address_book.get_employee_address(employee_id)
