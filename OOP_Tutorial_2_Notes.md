# Python OOP Tutorial 2: Class Variables

**Source:** [Corey Schafer - Python OOP Tutorial 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho)  
**Related Notes:** [OOP_Tutorial_1_Notes.md](file:///Users/navidrahman/Devs/Python/OOP_Tutorial_1_Notes.md)  
**Workspace File:** [oop.py](file:///Users/navidrahman/Devs/Python/oop.py)

---

## Table of Contents

1. [What Are Class Variables?](#1-what-are-class-variables)
2. [Instance Variables vs. Class Variables](#2-instance-variables-vs-class-variables)
3. [Example 1: The Annual Raise Amount](#3-example-1-the-annual-raise-amount)
   - [Why Hard-Coding Values Is Bad](#why-hard-coding-values-is-bad)
   - [Pulling It Out Into a Class Variable](#pulling-it-out-into-a-class-variable)
4. [Accessing Class Variables: Why `raise_amount` Alone Fails](#4-accessing-class-variables-why-raise_amount-alone-fails)
5. [How Attribute Lookup Works (Namespaces & `__dict__`)](#5-how-attribute-lookup-works-namespaces--__dict__)
6. [Modifying Class Variables: Class vs. Instance Level](#6-modifying-class-variables-class-vs-instance-level)
   - [Modifying via the Class (`Employee.raise_amount = 1.05`)](#modifying-via-the-class-employeeraise_amount--105)
   - [Modifying via an Instance (`emp_1.raise_amount = 1.05`)](#modifying-via-an-instance-emp_1raise_amount--105)
7. [Design Decision: `self.raise_amount` vs. `Employee.raise_amount`](#7-design-decision-selfraise_amount-vs-employeeraise_amount)
8. [Example 2: When NOT to Use `self` (`num_of_employees`)](#8-example-2-when-not-to-use-self-num_of_employees)
9. [Complete Code Reference](#9-complete-code-reference)

---

## 1. What Are Class Variables?

- **Class Variables** are variables that are **shared among all instances** of a class.
- While instance variables can be unique for each object (like `first`, `last`, `pay`, `email`), class variables remain the same across every instance unless explicitly overridden.
- Good candidates for class variables include:
  - Company-wide rates (e.g., annual raise percentage, interest rate, tax rate).
  - Class-wide counters or tracking metrics (e.g., total count of active users or created employees).
  - Default configurations or constants shared by all instances.

---

## 2. Instance Variables vs. Class Variables

| Feature | Instance Variable | Class Variable |
| :--- | :--- | :--- |
| **Defined** | Inside methods using `self.var_name = ...` | Directly in the class body outside methods |
| **Scope** | Unique to that specific object/instance | Shared by all instances of the class |
| **Memory** | Kept in the instance's own `__dict__` | Kept in the class's `__dict__` |
| **Access Syntax** | `self.var_name` or `instance.var_name` | `ClassName.var_name` or `self.var_name` |
| **Example** | `self.first = 'Navid'`, `self.salary = 50000` | `raise_amount = 1.04`, `num_of_employees = 0` |

---

## 3. Example 1: The Annual Raise Amount

Suppose our company gives employees an annual raise. The percentage might adjust every year, but in any given year, it applies across the company.

### Why Hard-Coding Values Is Bad

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        # HARD-CODED 4% (1.04)
        self.pay = int(self.pay * 1.04)
```

**Problems with hard-coding:**
1. **Hidden value:** `1.04` is buried inside the logic of `apply_raise()`. If used across multiple methods, you must hunt down every occurrence to change it.
2. **Cannot inspect:** You cannot easily check what the current raise amount is (e.g., `emp_1.raise_amount` or `Employee.raise_amount` does not exist).
3. **No flexibility:** You cannot easily customize the raise rate for an individual high-performer or subclass.

### Pulling It Out Into a Class Variable

We define `raise_amount` at the top level of the class body:

```python
class Employee:
    raise_amount = 1.04  # Class variable (4% raise)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
```

---

## 4. Accessing Class Variables: Why `raise_amount` Alone Fails

If you try to use `raise_amount` directly inside a method like this:

```python
def apply_raise(self):
    self.pay = int(self.pay * raise_amount)  # WRONG!
```

Python will throw an error:
```text
NameError: name 'raise_amount' is not defined
```

**Why?** In Python, class variables are **not** global variables. They are stored inside the class namespace.  
To access them inside methods or anywhere else, you must explicitly access them through:
1. **The class itself:** `Employee.raise_amount`
2. **Or an instance of the class:** `self.raise_amount`

---

## 5. How Attribute Lookup Works (Namespaces & `__dict__`)

You can access `raise_amount` from both the class and any instance:

```python
print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)     # 1.04
print(emp_2.raise_amount)     # 1.04
```

### The Lookup Chain:
When you request an attribute on an instance (e.g., `emp_1.raise_amount`), Python checks in this exact order:
1. **The Instance itself:** Does `emp_1` have `raise_amount` in its own dictionary (`emp_1.__dict__`)?
2. **The Class:** If not found on `emp_1`, does its class `Employee` have `raise_amount`?
3. **Parent Classes:** If not found on `Employee`, check any classes `Employee` inherits from.

### Inspecting Namespaces Using `__dict__`:

```python
print(emp_1.__dict__)
# {'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 'email': 'corey.schafer@company.com'}
# Notice: raise_amount is NOT in emp_1.__dict__!

print(Employee.__dict__)
# {..., 'raise_amount': 1.04, '__init__': <function ...>, 'apply_raise': <function ...>}
# raise_amount lives here in the class!
```

---

## 6. Modifying Class Variables: Class vs. Instance Level

This is one of the most critical OOP concepts in Python:

### Modifying via the Class (`Employee.raise_amount = 1.05`)

```python
Employee.raise_amount = 1.05

print(Employee.raise_amount)  # 1.05
print(emp_1.raise_amount)     # 1.05
print(emp_2.raise_amount)     # 1.05
```
> Changing the variable on the class changes it for the class **and for all instances** that inherit the lookup.

---

### Modifying via an Instance (`emp_1.raise_amount = 1.05`)

```python
emp_1.raise_amount = 1.05

print(Employee.raise_amount)  # 1.04 (Unchanged!)
print(emp_1.raise_amount)     # 1.05 (Changed ONLY for emp_1!)
print(emp_2.raise_amount)     # 1.04 (Unchanged!)
```

### Why did this happen?
When we ran `emp_1.raise_amount = 1.05`, Python did **not** modify the class variable.  
Instead, Python **created a new instance attribute** named `raise_amount` inside `emp_1.__dict__`!

Checking the namespace confirms this:
```python
print(emp_1.__dict__)
# {'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 'raise_amount': 1.05, ...}
```
Now, when accessing `emp_1.raise_amount`, Python finds `1.05` right away in `emp_1`'s own namespace and never needs to check the class.

---

## 7. Design Decision: `self.raise_amount` vs. `Employee.raise_amount`

Inside `apply_raise()`, which should we use?

```python
# Option A:
def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amount)

# Option B (RECOMMENDED for this case):
def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)
```

### Why Option B (`self.raise_amount`) is superior here:
1. **Per-instance customization:** It allows any individual instance to override their raise amount (e.g. `emp_1.raise_amount = 1.06`) and have `apply_raise()` respect that employee's custom rate.
2. **Subclass flexibility:** If we later create a `Developer` or `Manager` subclass, that subclass can easily override `raise_amount` without breaking `apply_raise()`.

---

## 8. Example 2: When NOT to Use `self` (`num_of_employees`)

What if we want to track the total number of employees created?

```python
class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

        # ALWAYS use the class name here:
        Employee.num_of_employees += 1
```

### Why use `Employee.num_of_employees` instead of `self.num_of_employees`?
- **Total count is strictly a class-level concept:** There is no scenario where an individual employee should hold a unique total company count.
- If you mistakenly wrote `self.num_of_employees += 1`:
  - Python would create an instance variable `num_of_employees = 1` on that specific object.
  - The shared counter on `Employee` would never increment past 0!

### Testing the Counter:
```python
print(Employee.num_of_employees)  # 0

emp_1 = Employee('Navid', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_employees)  # 2 (Incremented once per __init__ call!)
```

---

## 9. Complete Code Reference

```python
class Employee:
    # Class Variables
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance Variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

        # Increment class counter on every instantiation
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # Using self.raise_amount allows per-instance override
        self.pay = int(self.pay * self.raise_amount)


# 1. Demonstrating num_of_employees counter
print(f"Employees before creation: {Employee.num_of_employees}")  # 0

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(f"Employees after creation: {Employee.num_of_employees}")   # 2

# 2. Applying standard raise (using default class variable 1.04)
emp_2.apply_raise()
print(f"emp_2 pay after standard 4% raise: {emp_2.pay}")          # 62400

# 3. Overriding raise_amount for a single instance (emp_1 gets 5%)
emp_1.raise_amount = 1.05
emp_1.apply_raise()
print(f"emp_1 pay after custom 5% raise:   {emp_1.pay}")          # 52500

# 4. Checking namespaces
print(f"emp_1 dict contains raise_amount: {'raise_amount' in emp_1.__dict__}")  # True
print(f"emp_2 dict contains raise_amount: {'raise_amount' in emp_2.__dict__}")  # False
```
