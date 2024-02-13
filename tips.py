
# for i in range(5):
#     print(i)
#
# print("--- loop reached its end ")

for i in range(5):
    if i==3:
        break
    print(i)

print("--- loop reached its end ")

## actions ===> depends on loop completion without break

# for i  in range(10):
#     if i==5:
#         break
#     print(f"----> {i}")
# else:
#     print("--- this block will be executed if only loop wasn't broken")

for i  in range(10):
    if i==5:
        continue
    print(f"----> {i}")
else:
    print("--- this block will be executed if only loop wasn't broken")


name = "noha"
if name=="noha":
    pass  # when it is executed --> nothing happens
    # It is useful as a placeholder when a statement is required syntactically


print("---------------------------------")



# num = int(input("Enter a number: "))
# print(num)
#### Never Trust user input
# num = input("Enter a number: ")
# if num.isdigit():
#     num= int(num)
#     print(num)


while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    print("---- please try again")