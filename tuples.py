"""
tuple  is collection of items ===>
can hold different items from different datatypes
"""
# 
# "1- define  a tuple "
# 
t = ()
myt = tuple()
# 
""" tuple can hold different data from different datatypes"""
# 
myt = ("iti", "python", 34, (324.24, True), "iti", None , ["python", "flask", "odoo", "iti"], 234.23)
print(myt)
# 
""" get len of tuple """
print(len(myt))
# 
""" access element using index """
print(myt[3])
print(myt[6][1])
# 
""" count elements"""
print(myt.count("iti"))
# 
""" get index of element  ===> get index of the first occurrence of the element"""
print(myt.index("iti"))

""" for loop """
# index = 0
# for myelment in myt:
#     print(f"{index}: myelement = {myelment}")
#     index = index + 1

# """ get index of elements ---> enumerate """
tuple_indices =enumerate(myt)  # generate index for the iterator
print(tuple_indices)  # enumerate object
# for index, item in tuple_indices:
#     print(f"{index}:{item}")

""" cast enumerate object to a list """
items =list(tuple_indices)
print(items)
# 
# for index, char in enumerate("noha"):
#     print(f"{index}:{char}")
# 
""" check if element  exists on tuple or not """
print("iti" in myt)
# 
"""tuple is immutable datatype ===> modify its content """
print(myt)
# myt[4]="updated"  # TypeError: 'tuple' object does not support item assignment




""" concat the tuple """
t1 = ("js" , "css", 'html')
t2 = ("python", "postgres", 'flask')
courses = t1 + t2 # concat --> return with new tuple
print(courses)
# 



# 
""" cast string to a tuple """
name= "noha"
name = tuple(name)
print(name)  # ('n', 'o', 'h', 'a')

#
""" join tuple elements into one string """
data = ("My", "name","is", 'noha')
newstring = ":".join(data)
print(newstring)

""" tuple of one item """
tt = ("iti",)
print(tt, type(tt))