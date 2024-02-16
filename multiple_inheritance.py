
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class Child (A, B):
#     pass
#
# c = Child()
# print(isinstance(c, A), isinstance(c, B))


""" 2nd scenario """


# class A:
#     pass
#
#
# class B:
#     def __init__(self):
#         print("object B is being created ")
#
#
# class Child (A, B):
#     pass
#
# c = Child()
# print(isinstance(c, A), isinstance(c, B))
""" --------------------------- """
# class A:
#     def __init__(self):
#         print("object A is being created")
#
#
# class B:
#     def __init__(self):
#         print("object B is being created ")
#
#
# class Child (A, B):
#     pass
#
# c = Child()
# print(isinstance(c, A), isinstance(c, B))
#

""" -----------------------"""
class A:
    def __init__(self):
        print("object A is being created")
        self.name = ''

    def printObject(self):
        print(f"{self.name}")

class B:
    def __init__(self):
        print("object B is being created ")
        self.email = ""

    def add_city(self, value):
        self.city = value


class Child (A, B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("--- child is being created")

c = Child()
print(isinstance(c, A), isinstance(c, B))
c.add_city("New York")



