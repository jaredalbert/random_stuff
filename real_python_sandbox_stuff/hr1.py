class PayRollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for {employee.id} - {employee.name}')
            print (f'check amount: {employee.calculate_payroll()}')
            print('')
            
  
  
