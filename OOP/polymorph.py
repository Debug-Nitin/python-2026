# duck typing to achieve polymorphism
# operator overload + , __add__ method    int class int.__add__(self, other) a.__add__(b) a + b
# print calls __str__ method of the object to get its string representation

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"