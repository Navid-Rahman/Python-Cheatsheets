# Python object oriented programming
#
#


class Employee:

    def __init__(self, first, last, salary):
        # These are instance variables. They belong to this specific employee.
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@example.com'


    def fullname(self):
        # self.first and self.last come from the employee object that calls this.
        return '{} {}'.format(self.first, self.last)


# emp_1 and emp_2 are two separate instances of the Employee class.
emp_1 = Employee('Navid', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)

# Before using __init__, we would need to create every attribute manually:
# emp_1.first = 'Navid'
# emp_1.last = 'Rahman'
# emp_1.email ='navid.rahman@example.com'
# emp_1.salary = 50000

# emp_2.first = 'Jahidul'
# emp_2.last ='Alam'
# emp_2.email = 'jahidul.alam@example.com'
# emp_2.salary = 60000

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.fullname())
print(emp_2.fullname())
