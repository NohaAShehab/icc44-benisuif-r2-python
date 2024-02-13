""" functions with known number of arguments """
# def myfunction():
#     pass
#
# "call the function"
# res= myfunction()  # return with None
# print(res)

""" check this """
# def myfunction():
#     return
#
# "call the function"
# res= myfunction()  # return with None
# print(res)

""" function do somthing """
# def sayhello():
#     print("Hello from Ghaza")
#
# sayhello()

""" function return with result"""


def get_fullname():
    firstname = input("Enter firstName: ")
    lastname = input("Enter lastName: ")
    fullname = f"{firstname} {lastname}"
    return fullname


# myname = get_fullname()
# print(myname)

""" function accept arguments --> do operation , return result """

def sumnum(num1 ,num2):
    print(f"num1={num1} and num2={num2}")
    res = num1 + num2
    return res

# r = sumnum(23,23)
# print(r)

# print(sumnum(234,3434,4))

# ## functions with default arguments

# def sumnum2(num1,num2=10):
#     print(f"num1={num1}, num2={num2}")
#     return  num1 + num2
#
# print(sumnum2(3,5))
# print(sumnum2(43))
#
# print("noha", end='#')
# print("shehab")
#
# print("ahmed", "mohamed","ali", sep='||')
#

""" functions with unknown number of arguments """

print()
print("er")
print(34,23,235,324, 24)

## function accept variable number of arguments
def getnumbers(*nums):  # *---> represent zero or more argument
    print(nums)  # tuple


# getnumbers()
# getnumbers(34)
# getnumbers(3,435,3, "sjdfkh","jkshf")


""" """
def introduce_your_self(**info):
    print(info)  # dict

# introduce_your_self(name='noha', work='iti')
# introduce_your_self()
# introduce_your_self(fname='ahmed', lname='ali')
#
#
# temp ="my name is {username}, I works at {company}"
# print(temp.format(username="JK", company="Springfield"))






# def sumnum(num1, num2):
#     print(f"num1={num1} and num2={num2}")
#     print(f"{num1}+{num2}={num1+num2}")
#
# sumnum(4,5)
# sumnum("noha","shehab")
# sumnum("iti",4)


# def sumnum(num1:int, num2:int):  # for documentation purpose
#     print(f"num1={num1} and num2={num2}")
#     print(f"{num1}+{num2}={num1+num2}")
#
# sumnum(4,5)
# sumnum("noha","shehab")
# sumnum("iti",4)


""" check type of data """

print(isinstance("iti", str))
def sumnum(num1:int, num2:int):  # for documentation purpose
    if isinstance(num1, int) and isinstance(num2, int):
        print(f"num1={num1} and num2={num2}")
        print(f"{num1}+{num2}={num1+num2}")
        return num1+num2
    print("---- num1 and num2 must be integers ----")
    return None

sumnum(4,5)
sumnum("noha","shehab")
sumnum("noha",34)


