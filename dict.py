
""" data ==> label data -> key: value"""

info =["noha", 31, "iti"]
print(info)

""" create label datatype """
d = {}
myd = dict()

"""contain key:value pair
doesn't allow duplicate key
dict  --> is an ordered datatype 
"""
myinfo = {"name":"noha", "age":31, "work":"iti", "name":"Noha Shehab",
          "email":"noha@gmail.com"
          }
print(myinfo)
"access elements using key"
print(myinfo["name"])
"mutable datatype"
myinfo["work"] ="Information Technology Institute"
print(myinfo)

myinfo["city"]="Cairo"  # if keyword doesn't exists --> add key:value pair to the dict
print(myinfo)


""" get len of dict """
print(len(myinfo))

""" check if element exists in dict or not """
print(31 in myinfo)  # search if value exists in keys
print("name" in myinfo)
""" check in dict values """
d_keys = myinfo.keys()  # dict_keys
print(d_keys)
keys = list(d_keys)
print(keys)


d_values = myinfo.values()  # dict_values
print(d_values)
values = list(d_values)
print(values)

print(31 in myinfo.values())

""" for loop over the dict """

for abbass in myinfo:
    print(f"key={abbass},value={myinfo[abbass]} ")

"get dict and values "

myinfo_items = myinfo.items()
print(myinfo_items)

# myinfo_items = list(myinfo_items)
# print(myinfo_items)

for k , v in myinfo.items():
    print(f"{k}:{v}")

'update dict '
add_info = {"courses":['python', "postgres"], "work_days":7, "city":"GIZA"}
print(myinfo)
myinfo.update(add_info)
print(myinfo)



""" pop key:value pair"""
popped_value=myinfo.pop("name")
print(popped_value)
print(myinfo)


""" clear dict """
# myinfo.clear()

# del myinfo["city"]





