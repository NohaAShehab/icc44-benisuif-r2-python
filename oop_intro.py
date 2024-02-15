"""employees"""


# emp1 = {
#     "name":"ahmed",
#     'age': 25, 'salary':10000
# }
#
# emp2 = {
#     "fname":"Ali",
#     "empage":44,
#     "salary":10000
# }

def printEmp(emp):
    print(f"{emp['name']}, {emp['age']}, {emp['salary']}")


# printEmp(emp1)
# printEmp(emp2)

# print(emp2.values())
""" create datatype ---> sepcial architecture
define properties  ---> define methods 

"""

""" classes ---> 
    
    user defined data types --->
"""

"""1- define a class """

# class Employee:
#     pass
#
#
# # """ take an object """
# myobj = Employee()  # take an object from the class
# print(myobj)  # object address
#
# ## add properties to the object
# myobj.name=  'noha'
# myobj.salary =1000
#
#
# emp2 = Employee()
# emp2.name = 'Ahmed'
# emp2.city = "Cairo"
#
# print(isinstance(emp2, Employee))
# print(isinstance(myobj, Employee))


""" control object architecture """
# class Employee:
#     def __init__(self): # constructor function
#         print(f'object is being created {self}')
#         ## self represent object address
#
#
#
# emp1 = Employee()
# print(emp1)
# emp2= Employee()
# print(emp2)


""" object consists of sepcific properties """

# class Employee:
#     def __init__(self): # constructor function
#         # object ---> is an instance of the class
#         self.name = 'noha'
#         self.age = 0
#         self.salary =24789
# name, age, salary --> instance variables
#
#
# emp = Employee()
# print(emp.name)
# emp.name = "updated"
# emp.city = "Cairo"
# emp2 =Employee()
# emp3 = Employee()

""" customize object """

# class Employee:
#     def __init__(self, name ,age, salary):  # constructor function
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#
# emp = Employee("ahmed", 25, 10000)
# print(emp.name)
# emp.city = "cairo"

""" instance method """

# class Employee:
#     def __init__(self, name ,age, salary):  # constructor function
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     """ instance method represent behaviour related to the instance """
#     def speak(self):  # instance method ---> self ---> represent address of object
#         print(f"My name is {self.name}, I am {self.age} years old ")
#
# emp = Employee("ahmed", 25, 10000)
# print(emp.name)
# emp.city = "cairo"
# emp.speak()
#
# emp2 = Employee("Ali", 30, 10000)
# emp2.speak() # behaviour of speak depends on the caller instance
#


""" count no of instances taken from the class """

# class Employee:
#     "class variable --> represent class itself"
#     count = 0   # class variable
#     def __init__(self, name ,age, salary):  # constructor function
#         self.name = name
#         self.age = age
#         self.salary = salary
#         Employee.count +=1
#         self.id = Employee.count
#
#
#     def speak(self):  # instance method ---> self ---> represent address of object
#         print(f"My name is {self.name}, I am {self.age} years old ")
#
# print(Employee.count)
# """ class variable ---> its value depends on the class itself not instance
# can be accessed directly using class name
#
# shared property between all class instances
# """
#
# emp= Employee("ahmed", 23, 29408)
# emp2= Employee("Ali", 32, 28947)
#
# print(Employee.count)


""" class method """
# class Employee:
#     "class variable --> represent class itself"
#     count = 0   # class variable
#     def __init__(self, name ,age, salary):  # constructor function
#         self.name = name
#         self.age = age
#         self.salary = salary
#         Employee.count +=1
#         self.id = Employee.count
#
#
#     def speak(self):  # instance method ---> self ---> represent address of object
#         print(f"My name is {self.name}, I am {self.age} years old ")
#
#     ## define method return with no_of_employees
#     ## this function depends on the class not the instance
#     @classmethod
#     def printEmpCount(cls):  # first parameter of the function represent class
#         # print(cls)
#         print(cls.count)
#
#
#     def myfun(self):
#         pass
#
#     @classmethod
#     def myfunc(cls):
#         pass
#
#
# Employee.printEmpCount()
# emp = Employee("john", 34,2434)
# print(Employee.count)


"""

    class method used as object factory ---> //
    represent behaviour related to the class 
    ---> object creation 
"""
import json


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_default_teacher(cls):
        return cls("", 20)


# myt = Teacher("Ahmed", 23)
#
# teacherobj = Teacher.create_default_teacher()
# print(teacherobj)

# create default object

"""
    create instance from class --> saving instance in a file /// instance
    load all instances from file  /// class method

"""

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages


"""   ----------- check this scenario --------------"""


class Employee:
    def __init__(self, name, age, salary):  # constructor function
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod  # decorator used when the function neither depends on instance not the class
    def cal_net_sal(salary):
        net_salary = salary * 0.8
        print(f"net salary: {net_salary}")
        return net_salary


emp = Employee("noha", 22, 723489)
emp.cal_net_sal(87486)
Employee.cal_net_sal(emp.salary)
## to call static method
# print(Employee.cal_net_sal(23897489))
# print(Employee.cal_net_sal(emp.salary))
#
# ### cal net salary. print
# def cal_net_sal(salary):
#     net_salary = salary * 0.8
#     print(f"net salary: {net_salary}")
#     return net_salary
#
#
# cal_net_sal(emp.salary)
#
# cal_net_sal(1000000)
