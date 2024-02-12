
#
# name = 'noha'   # string
#
# email = "noha@gamil.com"  #string
#
# # this is a comment
#
# " nice to meet you all ===>" # this string can be treated as comment
#
# print(name)
# print(email)
#
# bio= ("My name is Noha"
#       "I works at ITI"
#       "I lives in cairo")
#
# print(bio)
#
# # keep the newlines in the string
#
# bio = '''My name is Noha
# I works at ITI
# I lives in cairo'''  # add \n at end of each line
# print(bio)
#
#
# """ interpreter detect datatype in the runtime """
#
# """ to get type of variable"""
#
# print(type(name))  # string
#
# age = 31
# happy = True
# g = 9.8
#************************ type conversion ****************************

age = 31
name= 'noha'
year = '2024'
track = 'python'
happy = True
g= 9.8

## convert from type to another

""" convert from int to sting"""
print(age, type(age))
age = str(age)
print(age, type(age))

""" convert bool to string """
happy =str(happy)
print(happy, type(happy))

""" convert str to int """
print(age, type(age))  # string
age = int(age) # int
print(age, type(age))


# track = int(track)  # ValueError: invalid literal for int() with base 10: 'python'
# you can only convert from string to int  --> in case of string is numeric string


num = 10
num +=5  # num = num +5


# ************************* logical operators ******************

print("iti" and "python" and 10)

print(bool("iti"))
print(bool("python"))
print(bool(10))

res=  "iti" and "" and 'noha'
print(res)

print(True and "iti" and 2000 and 10)

print("iti" or "ahmed" or 10000000000000000)
