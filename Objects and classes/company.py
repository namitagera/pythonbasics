from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.fname,i.lname)

    def paycheck(self):
        print("Paying employees")
        for i in self.employees:
            print("Paycheck for", i.fname, i.lname)
            print(f"Amount, ${i.calculate():,.2f}")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Ben", "Smith", 25, 50)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee("Bob", "Brown", 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display()
    my_company.paycheck()

main()