# Python OOP Tutorial 1: Classes and Instances

**Source:** [Corey Schafer - Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)  
**Workspace File:** [oop.py](file:///Users/navidrahman/Devs/Python/oop.py)

---

## Table of Contents

1. [Why Use Classes?](#1-why-use-classes)
2. [Classes vs. Instances (Objects)](#2-classes-vs-instances-objects)
3. [The `pass` Keyword](#3-the-pass-keyword)
4. [Instance Variables: Manual vs. Automatic Setup](#4-instance-variables-manual-vs-automatic-setup)
5. [The `__init__` Method and What `self` Really Means](#5-the-__init__-method-and-what-self-really-means)
6. [Adding Methods (Actions) to a Class](#6-adding-methods-actions-to-a-class)
7. [Common Mistakes & Gotchas](#7-common-mistakes--gotchas)
8. [Behind the Scenes: How Python Executes Method Calls](#8-behind-the-scenes-how-python-executes-method-calls)
9. [Complete Code Reference](#9-complete-code-reference)

---

## 1. Why Use Classes?

- **Logical Grouping:** Classes allow us to logically bundle related **data** and **functions** together.
- **Reusability & Modularity:** Instead of writing repetitive code, a class serves as a reusable template to produce similar objects.
- **Real-World Modeling:** Allows you to model entities (such as an `Employee`, `User`, `Car`, or `BankAccount`) naturally with their own characteristics and capabilities.

### Key Terms:

| Term                  | Definition                                            | Example                                   |
| :-------------------- | :---------------------------------------------------- | :---------------------------------------- |
| **Class**             | The blueprint or prototype for creating objects       | `Employee`                                |
| **Instance (Object)** | A concrete item created from that blueprint           | `emp_1`, `emp_2`                          |
| **Attribute**         | A variable belonging to a class or an instance (data) | `self.first`, `self.email`, `self.salary` |
| **Method**            | A function belonging to a class (action)              | `def fullname(self):`                     |

---

## 2. Classes vs. Instances (Objects)

- A **Class** is the architectural blueprint of a house.
- An **Instance** is the actual physical house built using that blueprint.
- Each instance has its own distinct address in computer memory:

```python
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)  # <__main__.Employee object at 0x10229dd30>
print(emp_2)  # <__main__.Employee object at 0x10227e350>
```

> Notice the memory addresses (the hexadecimal IDs at the end) are different. `emp_1` and `emp_2` are separate entities.

---

## 3. The `pass` Keyword

If you want to create an empty class or function as a placeholder without writing its implementation right away, Python requires a statement inside its block to avoid an `IndentationError`:

```python
class Employee:
    pass  # Tells Python: "Skip for now, no-op placeholder"
```

---

## 4. Instance Variables: Manual vs. Automatic Setup

### The Manual Approach (Why You Shouldn't Do It)

You can manually attach attributes to instances after creating them:

```python
emp_1 = Employee()
emp_1.first = 'Navid'
emp_1.last = 'Rahman'
emp_1.email = 'navid.rahman@example.com'
emp_1.salary = 50000

emp_2 = Employee()
emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@example.com'
emp_2.salary = 60000
```

### Why manual creation is bad:

1. **Too much boilerplate:** You have to re-type every attribute line for each new employee.
2. **Prone to typos/bugs:** You might accidentally write `emp_1.last = 'User'` while creating `emp_2`.
3. **Defeats OOP principles:** It doesn't use the class blueprint to enforce structure.

---

## 5. The `__init__` Method and What `self` Really Means

### What is `__init__`?

- Stands for **initialize**.
- In other languages (like C++, Java, C#), this is called a **Constructor**.
- It runs **automatically** every time a new instance of the class is created.

```python
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{first.lower()}.{last.lower()}@example.com"
```

### What is `self`?

- `self` represents the **specific instance currently being created or operated on**.
- When you instantiate:
  ```python
  emp_1 = Employee('Navid', 'Rahman', 50000)
  ```
  Python automatically passes `emp_1` into `__init__` as `self`.
- Inside `__init__`:
  - `self.first = first` literally becomes `emp_1.first = 'Navid'`
  - `self.last = last` literally becomes `emp_1.last = 'Rahman'`
  - `self.salary = salary` literally becomes `emp_1.salary = 50000`

> **Note on naming:** The attribute name does not _have_ to match the parameter name (e.g. `self.fname = first` works), but keeping them identical is PEP 8 standard practice.

---

## 6. Adding Methods (Actions) to a Class

Instead of manually string-formatting outside the class every time you need an employee's full name:

```python
# Manual way (cumbersome and repetitive):
print('{} {}'.format(emp_1.first, emp_1.last))
```

We define an **instance method** inside the class:

```python
class Employee:
    ...
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
```

Now, calling the method is clean and reusable:

```python
print(emp_1.fullname())  # Navid Rahman
print(emp_2.fullname())  # Test User
```

---

## 7. Common Mistakes & Gotchas

### Mistake 1: Forgetting `self` in Method Definitions

```python
# WRONG:
class Employee:
    def fullname():
        return f"{self.first} {self.last}"
```

When you run `emp_1.fullname()`, Python raises:

```text
TypeError: fullname() takes 0 positional arguments but 1 was given
```

**Why?** Even though your call looks empty (`emp_1.fullname()`), Python automatically passes `emp_1` as the 1st argument. Because `fullname()` wasn't defined to accept arguments, it throws an error.

### Mistake 2: Forgetting the Parentheses `()` When Calling Methods

```python
print(emp_1.fullname)
# Output: <bound method Employee.fullname of <__main__.Employee object at 0x...>>

print(emp_1.fullname())
# Output: Navid Rahman
```

- Without `()`: You are referencing the **method object itself**.
- With `()`: You are **calling / executing** the method to receive its return value.

---

## 8. Behind the Scenes: How Python Executes Method Calls

These two lines do the exact same thing:

```python
# 1. Calling via the instance (standard and recommended)
emp_1.fullname()

# 2. Calling via the class name directly
Employee.fullname(emp_1)
```

### What happens under the hood:

When you execute `emp_1.fullname()`, Python internally converts it into:

```python
Employee.fullname(emp_1)
```

- When called from the class `Employee`, Python does not know which instance you want to operate on, so you **must manually supply `emp_1`** as the `self` argument.
- When called on `emp_1`, Python automatically injects `emp_1` into `self`.

---

## 9. Complete Code Reference

This is the clean pattern implemented in your [oop.py](file:///Users/navidrahman/Devs/Python/oop.py):

```python
class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Creating separate instances
emp_1 = Employee('Navid', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Accessing attributes
print(emp_1.email)      # Navid.Rahman@example.com
print(emp_2.email)      # Test.User@example.com

# Calling methods
print(emp_1.fullname()) # Navid Rahman
print(emp_2.fullname()) # Test User
```
