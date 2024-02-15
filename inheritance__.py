
# class Person:
#     pass
#
# p = Person()
#
# print(isinstance(p, object))
# # class Employee ---> inherits from Person
# class Employee(Person):
#     pass
#
# emp = Employee()
# print(isinstance(emp, Person))
# print(isinstance(emp, object))

""" customize object creation """
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
# class Employee(Person):
#     pass
#
# emp = Employee("noha")
# print(isinstance(emp, Person))
# print(isinstance(emp, object))
# emp.speak()



""" second scenario """
class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")

class Employee(Person):
    def __init__(self, name, salary):
        # call parent constructor
        super().__init__(name)
        self.salary = salary

    def speak(self):
        super().speak()  # call speak from parent
        print(f"My salary is {self.salary}")  # then execute this

emp = Employee("noha", 398123)
emp.speak()



"""overriding  ---> 2 functions with same name in 2 classes 
have inheritance relation
"""











