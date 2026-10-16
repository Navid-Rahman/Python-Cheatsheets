# Python object oriented programming
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        # These are instance variables. They belong to this specific employee.
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@example.com'

        Employee.num_of_emps += 1

    def fullname(self):
        # self.first and self.last come from the employee object that calls this.
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


print(Employee.num_of_emps)

# emp_1 and emp_2 are two separate instances of the Employee class.
emp_1 = Employee('Navid', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)


# print(emp_1.salary)
# emp_1.apply_raise()
# print(emp_1.salary)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# print(emp_1.__dict__)
# print(Employee.__dict__)

# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


print(Employee.num_of_emps)