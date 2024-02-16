
# class Employee:
#     def __init__(self, name, salary):
#         self.name =name
#         self.salary = salary
#
#     def __str__(self):
#         """ this function must return with string"""
#         return f"{self.name}"
#
#
# emp = Employee("John", 100000)
# print(emp)

"""2nd option """
# class Employee:
#     def __init__(self, name, salary):
#         self.name =name
#         self.salary = salary
#
#     def __str__(self):
#         return f"{self.name}"
#     def __repr__(self): # for development
#         "return string"
#         return f"Employee(name={self.name}, salary={self.salary})"
#
# emp = Employee("John", 100000)
# print(emp)
# print(emp.__repr__())


l = ["apple", "banana", "cherry"]
print(len(l))

# class Employee:
#     def __init__(self, name, salary):
#         self.name =name
#         self.__salary = salary
#
#     def __str__(self):
#         return f"{self.name}"
#     def __repr__(self): # for development
#         "return string"
#         return f"Employee(name={self.name}, salary={self.__salary})"
#
#     def __len__(self):
#         """ return number"""
#         return len(self.__dict__)
#
#     def __call__(self):
#         print("object is being called")
#


# emp = Employee("Anna", 100000)
# emp.city = 'cairo'
# print(len(emp))
#
# print(emp.__dict__)  # represent object inform of dict
#
# emp()






""" """


class Employee:
    __slots__ = ('name', 'salary', '__dict__')
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary
        self.__dict__ = {
            "name":self.name,
            "salary":self.salary
        }

    def __str__(self):
        return f'{self.name}'


emp = Employee("ahmed",324323)
# emp.city = "Cairo"
print(emp.__dict__)

print(emp)



