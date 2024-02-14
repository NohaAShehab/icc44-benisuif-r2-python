
"""
    syntax ---> parser --> must be resolved
    runtime error --> exceptions ---> unexpected event cause the program to stop
    logical error ---> application works but with wrong results
"""
""" logical"""
# def sumnum(num1, num2):
#     return num1 * num2
#
# print(sumnum(2,2))
# print(sumnum(3,4))

### test --> your work while development
## unit testing  --> test cases for your work ---> test cases --> before code


# ==> "may cause exception"


# print(name)  # NameError: name 'name' is not defined

# print(5/0)  # ZeroDivisionError: division by zero

# print("ahmed"+10)  # TypeError: can only concatenate str (not "int") to str

# num = int(input("Enter a number: "))  # ValueError: invalid literal for int() with base 10: 'gjhagd'

""" first case """
# try:
#     print(name)
# except:
#     print("--- problem happened")
#
# print("000000")

""" second case """
# try:
#     print(7/0)
# except:
#     print("--- problem happened")
#
# print("000000")


"""get exception info """

# try:
#     print(7/0)
# except Exception as e :
#     print(f"--- problem happened {e}")
#
# print("000000")

# try:
#     print(name)
# except Exception as e :
#     print(f"--- problem happened {e}")
#
# print("000000")

""" :exception handing ---> solve the problem"""

# try:
#     num = int(input("Enter a number "))
# except Exception as e:
#     print(e)
#     print("---- num must be number and setted to 0 ")
#     num =0
#
# print(num*10)
""" """
#
# try:
#     num = int(input("Enter a number "))
#     res = 10/num
# except ValueError as ve :
#     print(ve)
#     num = 1
#     res = 10/num
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 1
# except Exception as e:
#     print(e)
""" """

# try:
#     num = int(input("Enter a number "))
#     res = 10/num
# except Exception as e:
#     print(e)
# except ValueError as ve :
#     print(ve)
#     num = 1
#     res = 10/num
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 1

""" try except else  finally """
# try:
#     num = int(input("Enter a number "))
#     res = 10/num
# except Exception as e:
#     print(e)
# else:
#     print("This block will be executed only if there is no problem")
#     print(num ,res )
#
# finally:
#     print("----- this block will be executed always ")
#
# print("---------------------------------------------")

# why we need finally ??











def askforInt(message="please enter number: "):
    try:
        num=int(input(message))
    except Exception as e:
        print("==== invalid number")
        return  False
    else:
        return  num
    finally:
        print('=========process executed succsessfully====')

    print("---------------------")

print(askforInt())



class CustomInheritance(Exception):
    pass














