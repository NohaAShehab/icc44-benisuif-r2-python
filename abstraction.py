
"""
    abstract class ?
    goal ?
    define structure without implementation ---

        abstract class classname{
            abstract function functionname(){

            }
        }

"""

"""
    to define abstract class 
    1- inherit from class  --> ABC 
    2- create abstract function --> @abstractmethod
"""
### abc --> abstract base class
from abc import ABC, abstractmethod
""" to define abstract method --> class must inherit from ABC and contains abstract method"""
# class AbstractEmployee(ABC):
#
#     @abstractmethod
#     def speak(self):
#         pass
#
# emp = AbstractEmployee()
#"TypeError: Can't instantiate abstract class AbstractEmployee with abstract method speak"



""" """

# class AbstractEmployee(ABC):
#     pass
#
#
#
# emp = AbstractEmployee()
# print(emp)


# class AbstractEmployee:
#     @abstractmethod
#     def speak(self):
#         pass
#
#
#
# emp = AbstractEmployee()
# print(emp)



""" -------------------------- """

class AbstractEmployee(ABC):

    @abstractmethod
    def speak(self):
        pass

class Engineer(AbstractEmployee):

    def speak(self):
        print("I am Engineer")

eng = Engineer()
eng.speak()




