"""you can generate range of numbers """

nums =range(10)
print(nums) # range object
""" 
    start :0
    step :1
    stop:10
"""
# for i in nums:
#     print(f"i ={i}")   # i --> range (0-->9)

myrange= range(1, 10, 2)
print(list(myrange))


myr = range(100,1, -10)
print(list(myr))