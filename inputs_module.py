def askforInt(message="please enter an integer"):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("-- incorrect number--- please try again ---")


def askforString(message="please enter string"):
    while True:
        inputstr = input(message)
        if inputstr.isalpha():
            return inputstr
        print("---- Error / try again ------")

print("--------------------------------------------------")
##### this part must run only when inputs_module run
if __name__ == "__main__":
    # askforInt("please enter year : ")
    # print("-----------------welcome to input module---------------------------")
    # print(askforString("39ripoe"))
    # print(askforInt("please enter salary"))
    print('---- abaaaaaaaaaaassssssss')

# name= 'noha'