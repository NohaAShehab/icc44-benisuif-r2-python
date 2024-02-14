"""
    any .py file is considered to be a python module
"""

""" import module """

# import inputs_module
#
# print(inputs_module.askforInt("please enter age "))

""" alias module name """
#
# import inputs_module as myin
# print(myin.askforInt("please enter age "))

""" import part of the module """
# from inputs_module import  askforInt
# print(askforInt())

"""alias function name """
# from inputs_module import  askforInt as enternum
# print(enternum("Enter a number"))
# name = "noha"

# from inputs_module import  askforString
# print(askforString("jsdhfjkh"))

""" import from package"""

""" import module from package """

# import iti.greeting_modulle
# iti.greeting_modulle.say_hello("Ahmed")
# import iti.greeting_modulle as mymodule
# mymodule.say_hello("Ali")

""" import block from module"""
#
# from iti.greeting_modulle import  say_hello
# say_hello("Ali")

"""====> __init__"""
# import  mypkg  # calling the __init__
#
# mypkg.welcome('3109283')


# from mypkg.validation_modulle import  validateNumber
# print(validateNumber(32))


from mypkg import validateNumber
print(validateNumber(3423))