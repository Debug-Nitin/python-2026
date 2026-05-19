# instance method when we want to access the instance variable of class
# class method when we want to access the class variable of class defined using @classmethod decorator
# every class in python is a child class and inerits from a class called 'object'

class Employee:
    company = "Google"  # class variable

    def __init__(self, name, salary):
        self.name = name  # instance variable
        self.salary = salary  # instance variable

    def show(self):  # instance method
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    @classmethod
    def change_company(cls, new_company):  # class method
        cls.company = new_company