

message = 'we love python'


"1- get len of string "
print(len(message))

"2- count char occurence ? "

print(message.count('o'))

"3- check if char occurs in the string "
print("n" in message)

"4- you access string parts using index --> start from 0 "
print(message[4])

print(message[4:]) # slicing
print(message[4:10])
print(message[4:10:2])
print(message[::])
print(message[::-1])

""" -- string is immutable datatype -- """
""" concat strings --> only string  """
firstname= "noha "
midname= 'Abd Elhady '
lname = 'Shehab'
fullname = firstname+midname+ midname+lname + str(10)  #+ operator --> return new string
print(fullname)

" string interpolation"
fullname = firstname + midname *2 + lname
print(fullname)


""" formating the string """
no_of_students = 24
course_name  = 'python'

tempstring = "we have {0} students in course {1}"
print(tempstring)
#
#
# ## print string formated with values
#
# newstring = tempstring.format(no_of_students, course_name)  # return new string
# print(newstring)
#
# print(tempstring.format(course_name, no_of_students))
#
tempstring = "we have {anynumber} students in course {anycourse}"  # formatting string based on
# # keyword argument
#
# print(tempstring.format(anynumber=no_of_students, anycourse=course_name))


### f-format string
""" formatting string based on existing variables """
no_of_students = 24
course_name = "Math"
temp = f"we have {no_of_students} in {course_name} course "
print(temp)

""" upper lower title capitalize """

name = 'ali mohamed'
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

""" loop over the string """

message= "HelloGhaza"
for abbass in message:
    print(f"char = {abbass}")

""" get index of each char """
print(message.index('a'))  # index function return with the index of first occurrence of the char

# for abbass in message:
#     print(f"char = {abbass}, {message.index(abbass)}")

index = 0
for abbass in message:
    print(f"char = {abbass}, {index}")
    index +=1

num = "100"  # string
""" check status of string ? """

""" consists only from numbers"""
print(num.isdigit())
print(num.isnumeric())
# return true if string is numeric string ===> 0---9



""" consists only from alphas --> a-zAZ> with no spaces"""

print("noha".isalpha())
print("noha shehab".isalpha())
""" is all in upper / lower / title """
name= 'ahmed'
print(name.isupper())
print(name.islower())
print(name.istitle())

""" isspace """
message = "              "
print(message.isspace())  # return True only if string consists from spaces only

print("".isspace())

print("noha shehab".isspace())

print("noha shehab".count(" "))


""" accept string from user """
""" input function always returns with string """
# inputmessage = input("please leave the message: ")  # string
# print(inputmessage, type(inputmessage))


""" operations on string """
""" strip the string """
message = "          Nice to meet you              "
print(message, len(message))
newmessage = message.strip()  # remove spaces from the beginning and the end of the string
print(newmessage, len(newmessage))

print(message.lstrip())
print(message.rstrip())

""" strip special char ? """

message =  "  My name is Noha  a a a a"
print(message.strip("a M"))  # accept set of char we want to strip

""" replace """
print(message.replace("a", "@"))  # replace all chars --> a , @
print(message.replace("a", "@", 2))


###
a, b, c, d = 10, 66.66, 76.3, 100.54

print(round(c))

### min and max of string

###### while loop

num = 5

while num > 0:
    print(num)
    num -=1



# "noha" ---> 2

""" hgjg iti iti """  # 2


""" noha  =====> nh """

" iti ---> 0 2"

""