"""
list  is collection of items ===>
list --> most versatile data type in python--->
can hold different items from different datatypes
"""

"1- define  a list "

l = []
myl = list()

""" list can hold different data from different datatypes"""

myl = ["iti", "python", 34, 324.24, True, "iti", None , ["python", "flask", "odoo", "iti"], 234.23]
print(myl)

""" get len of list """
print(len(myl))

""" access element using index """
print(myl[3])
print(myl[7][1])

""" count elements"""
print(myl.count("iti"))

""" get index of element  ===> get index of the first occurrence of the element"""
print(myl.index("iti"))

""" for loop """
# index = 0
# for myelment in myl:
#     print(f"{index}: myelement = {myelment}")
#     index = index + 1

""" get index of elements ---> enumerate """
list_indices =enumerate(myl)  # generate index for the iterator
print(list_indices)  # enumerate object
for index, item in list_indices:
    print(f"{index}:{item}")

for index, char in enumerate("noha"):
    print(f"{index}:{char}")

""" check if element is exists on list or not """
print("iti" in myl)

"""list is mutable datatype ===> modify its content """
print(myl)
myl[4]="updated"  # update element using index
print(myl)


# myl[100] = "new element "  # IndexError: list assignment index out of range
"add elements to the list ? "
"append"
myl.append("python")  # append the element at the end of the list
print(myl)
""" insert item in certain position"""
myl.insert(5, "inserted_element")
print(myl)

"""pop element from the list """
popped_item=myl.pop()  # pop the last element from the list
print(myl)
print(popped_item)

'pop item at index'
popped_item=myl.pop(4)  # pop the last element from the list
print(myl)
print(popped_item)

"remove element from the list ? "
myl.remove("iti")
print(myl)

""" concat the list """
l1 = ["js" , "css", 'html']
l2 = ["python", "postgres", 'flask']
courses = l1 + l2 # concat --> return with new list
print(courses)

""" extend list with another ? """
print(l1)
l1.extend(l2)
print(l1)

""" sort a list --> comparison ===> > list elements must be from the same type """
# myl.sort()  #TypeError: '<' not supported between instances of 'int' and 'str'
print(f"courses: {courses}")
# courses.sort()  # sort ascending
# print(f"courses: {courses}")
courses.sort(reverse=True)  # sort descending
print(f"courses: {courses}")

""" reverse a list """
print(myl)
myl.reverse()
print(myl)

""" cast string to a list """
name= "noha"
name = list(name)
print(name)  # ['n', 'o', 'h', 'a']

""" split string to a list """
message = "my name is noha"
message = message.split(" ")
print(message)
""" join list elements into one string """
data = ["My", "name","is", 'noha']
newstring = "_".join(data)
print(newstring)