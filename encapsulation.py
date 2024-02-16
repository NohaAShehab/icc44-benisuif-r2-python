"""
    encapsulation

    ---> levels of accessibility
    keywords:
        public :: property/function public
                ---> can be accesses using instance // object anywhere
                --> in class --> self
                ---> out the class ---> object name

        protected :: property/function protected
            --> can be accessed using instance // object only in the class or derived class
            ==? self

        private: property/function private
        --> can be accessed only via instance // object only in the class
        ==? self

        " in python =========> NO ACCESS MODIFIERS "
        use names of variable define accessibility
        a-z  ============> public
        _[a-z] ===========> protected
        __[a-z]  ============> private

"""

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary =salary


#
# emp = Employee("Ahmed", "Ahmed@gmail.com", 8126)
# print(emp.name)
# emp.name ='updated'
#
# """ protected """
# print(emp._email)  # Ethically  don't do that
# emp._email = "updated@gamil.com"
#
# """ private """
# # print(emp.__salary)
# # print(emp.city)
# print(emp._Employee__salary) # Ethically  don't do that


" access private , protected ===> setter and getters "


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary * .7
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             # raising exception
#             raise ValueError("Salary must be integer ")
#
#
# emp = Employee("Mohamed", "wewee", 3897)
# print(emp.get_salary())
# # emp.set_salary("iti")
# emp.set_salary(89347)
# emp.name=  "Ali"
# # emp._Employee__salary = 'iti'
""" property """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary * .7
#
#     @property
#     def salary(self):
#         return self.__salary*0.7
#
#     @salary.setter
#     def salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             # raising exception
#             raise ValueError("Salary must be integer ")
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             # raising exception
#             raise ValueError("Salary must be integer ")
#
#
# emp = Employee("Mohamed", "wewee", 3897)
# # print(emp.get_salary())
# print(emp.salary)  # property
# print(emp.name)
# # emp.salary = "iti"
# emp.salary = 47236486
# emp.name=  "873r987rw"

""" -------------------> check this scenario """


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         # self.__salary = salary
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             # raising exception
#             raise ValueError("Salary must be integer ")
#
#     @property
#     def salary(self):
#         return self.__salary*0.7
#
#     @salary.setter
#     def salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             # raising exception
#             raise ValueError("Salary must be integer ")
#
#
#
# emp = Employee("Mohamed", "wewee", "iti")
# print(emp.salary)
#
# # emp = Employee("Mohamed", "wewee", 3897)
# # emp.salary = 837284
# # print(emp.salary)



""
class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        # self.__salary = salary
        self.salary = salary  # call salary setter while creating object

    @property
    def salary(self):
        return self.__salary*0.7

    @salary.setter
    def salary(self, salary):
        if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
            self.__salary = salary
        else:
            # raising exception
            raise ValueError("Salary must be integer ")

    @property
    def commission_rate(self):
        return 1.5 * self.salary


emp = Employee("Mohamed", "wewee", 10000)
print(emp)

print(emp.commission_rate)
# emp.commission_rate = 43435
emp.city = "erer"
























