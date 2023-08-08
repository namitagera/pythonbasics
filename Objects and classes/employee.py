class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate(self):
        return self.salary/52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hours, rate):
        super().__init__(fname, lname)
        self.hours = hours
        self.rate = rate

    def calculate(self):
        return self.hours * self.rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sale_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sale_num
        self.com_rate = com_rate


    def calculate(self):
        regualarsalary= super().calculate()
        totalcom = self.sales_num * self.com_rate

        totalsalary = regualarsalary + totalcom
        return totalsalary

    