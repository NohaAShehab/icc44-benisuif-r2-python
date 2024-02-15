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

class Employee:
    def __init__(self, name ,age, salary):  # constructor function
        self.name = name
        self.age = age
        self.salary = salary

    """ instance method represent behaviour related to the instance """
    def speak(self):  # instance method ---> self ---> represent address of object
        print(f"My name is {self.name}, I am {self.age} years old ")

emp = Employee("ahmed", 25, 10000)
print(emp.name)
emp.city = "cairo"
emp.speak()

emp2 = Employee("Ali", 30, 10000)
emp2.speak() # behaviour of speak depends on the caller instance








