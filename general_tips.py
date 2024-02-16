""" create function for instant use  --> only used in this place """

myarray = [4, 5, 6, 10, 23, 24, 55]

# lambda --> anonymous function
# res = filter(lambda element: element%2==0, myarray)
# print(res)
# res = list(res)
# print(res)

myres = map(lambda item: item * 4, myarray)
print(myres)  # map object
myres = list(myres)
print(myres)

""" list comprehension"""
# generate list in one line

# myl = [num for num in range(10)]
# print(myl)

# myl = [num for num in range(10) if num%2==0]
# print(myl)

# myl = [num for num in range(10) if num%2==1]
# print(myl)


""" ----------> iteration """
mylist = [1, 2, 3, 4, 5, "apple", 'kiwi']

# for item in mylist:
#     print(f"item = {item}")

## creater iterator
mylist_iter = iter(mylist)  # list_iterator
print(next(mylist_iter))
print(next(mylist_iter))
print(next(mylist_iter))
print(next(mylist_iter))
print(next(mylist_iter))
print(next(mylist_iter))
print(next(mylist_iter))
# print(next(mylist_iter)) # stop iterator

#####
"check if all elements in list/tuple represent True"
# print(all([345,34,345,"iti", True, 0]))
print(any([345,34,345,"iti", True, 0]))















