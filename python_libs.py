# math lib ?

# import math
# print(math.pi)
# print(math.ceil(4324.23))

""" os lib """
import os

print(os.getcwd())
print(os.getlogin())
os.system("ls -l")
# os.system("sudo systemctl restart apache2 ")
# os.system("sudo systemctl status apache2 ")

# os.mkdir("oop")

# os.rmdir("oop")

print(os.getenv("SHELL"))

# print(input("please enter value "))
# os.system("clear")


## coloring the terminal
def prPurple(skk):
    print("\033[95m {}\033[00m" .format(skk))

# prPurple("ITI")



""" re module """
## function regex
import re

# email = input("please enter email: ")

# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
""" 
    match return with match object if the the first part of the string 
    match the pattern 

"""
# res = re.match(pattern, email)
# print(res)
# if res:
#     print("--- valid email ---")
# else:
#     print("Email not valid ")

# "noha@gmail.com.iti"


""" check if whole the string matches the pattern """
# res = re.fullmatch(pattern, email)
# print(res)
# if res:
#     print("--- valid email ---")
# else:
#     print("Email not valid ")


""" time // datatime """

import time
print(time.time())  # time stamp inform of number of seconds
# timestamp --> no of seconds 1970 ---


## start/end data --> based on time

import datetime
now = datetime.datetime.now()
print(now)
current_date = datetime.date.today()

print(current_date)

"""built-in lib """


"""external lib --> install ---> pip """
