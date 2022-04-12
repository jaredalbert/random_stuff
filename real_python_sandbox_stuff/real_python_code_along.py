class PayROllSystem:
    def calculate_payrol(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payrool for {employee.id}')
            
        
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    #pass
    def __init__(self, id, name, weekly_salary):
        self.weekly_salary=weekly_salary
        super().__init__(id, name)
        
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hours_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hours_rate
        super().__init(id, name)
    
    def calculate_payroll(self):
        return(self.hours_worked * self.hours_rate)
    
class CommissionEmployee(Employee):
    def __init__(self, id, name, commission):
        super().__initi__(id, name)
    
    

