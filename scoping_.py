#************* global scope

coursename = 'python'   # scope global scope

print(f"coursename={coursename}")

#*********************************
def mynewfun():
    name="ali"  # local variable => defined inside the function
    print(f"name= {name}")

# mynewfun()
# print(name)

##################################################
""" access global variable from inside the function"""

content = "lexical scoping"

def printContent():
    print(f"from function {content}")

# printContent()


""" modify global variable  from inside the function"""

# def modifyContent():
#     content = "functions and datatypes "  # new local variable
#     print(content)
#
# modifyContent()
# print(content)

num = 10
def modifyContent():
    global content
    global  num
    content = "functions and datatypes "  # modify global one
    num +=1
    print(content)
print(content)
modifyContent()
# print(content)


""" function inside a function """
# def outerfunction():
#     coursename = 'python'  # local variable
#     # can be access anywhere inside the function
#
#     def innerfunction():
#         print(f"from inner coursename = {coursename}")
#
#     innerfunction()
#     print(coursename)
#
# outerfunction()


""" modify local variable  from inside the inner  function"""

# def outerfunction():
#     coursename = 'python'  # local variable
#     # can be access anywhere inside the function
#
#     def modify_course():
#         coursename = "django" # new local variable
#         print(f"from inner coursename = {coursename}")
#
#     modify_course()
#     print(coursename)
#
# outerfunction()


# def outerfunction():
#     coursename = 'python'  # local variable
#     # can be access anywhere inside the function
#
#     def modify_course():
#         nonlocal coursename # don't create new variable use the local of the parent
#         coursename = "django" #
#         print(f"from inner coursename = {coursename}")
#
#     modify_course()
#     print(coursename)

# outerfunction()


def outerfunction():
    coursename = 'python'  # local variable
    # can be access anywhere inside the function

    def modify_course():
        global coursename # don't create new variable
        coursename = "django" #
        print(f"from inner coursename = {coursename}")

    modify_course()
    print(coursename)

outerfunction()




# lab
"""
    3 
    [
        [1],   1*1
        [2,4],  2*1 --> 2*2
        [3,6,9]  3*1, 3*2, 3*3
    ]

(3,7) ==> [7,8,9]

noha ---> ahon

re ---> re.match() --> validation regular expression

'abdulrahman'
abdu
lr
ahm
an
--------------------------------------------------------
(apple, banana, kiwi)
noha 
hi noha 
------
k
------
a
-a-a-a

"""
















