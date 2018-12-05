class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)




class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang
    raise_amt = 1.10



class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())


dev_1=Developer("ahijeet","kumar",50000,'python')
dev_2=Developer("abhishek","Kumar",60000,'java')

print("\nTo check where python will search for the method and attributes")
print(help(Developer))
print("\n Both developers email")
print(dev_1.email)
print(dev_2.email)

print("\n Working on raise method")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print("\nfirst developer programming language")
print(dev_1.prog_lang)

print("\nWorking in Manager Class")
mgr_1=Manager("Sue","Smith",90000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print("\nChecking out isinstance and issubclass builtin class")
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))