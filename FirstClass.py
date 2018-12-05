class Employee:
    num_of_empls=0
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last = last
        self.pay = pay
        self.email= first + last + "@gmail.com"
        Employee.num_of_empls +=1

    def fullname(self):
         print(f'Full name is {self.first} {self.last}')


    def  apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

emp1=Employee("ahijeet","kumar",50000)
emp2=Employee("abhishek","Kumar",60000)

'''print(emp1)
print(emp2)'''

Employee.fullname(emp1)

print("Is same as")

emp1.fullname()

print("\nWorking on the apply_raise Function")
emp1.apply_raise()
print(emp1.pay)
print(emp1.raise_amount)

print("\nChecking out the attributes of class Employee and instance emp1")
print(Employee.__dict__)
print(emp1.__dict__)


print("\nDifference b/w accessing a variable through class name and Instance name")
Employee.raise_amount=1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("\nIf we change the value with a instance , then only for that instance the value will be changed")
emp1.raise_amount=1.99
print(emp1.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(f'No of Employees is {Employee.num_of_empls}')



















