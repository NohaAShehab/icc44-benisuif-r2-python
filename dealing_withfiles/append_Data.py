"""
    open ---> open file
    mode ==> "a"  ---> if file doesn't exist --> python will try
     to create

     when you open file with a--> mode --> open file for appending
     starting from the end of the file === keep old content
"""

try:
    fileobject= open("mycv2.txt", "a")
except Exception as e:
    print(e)
else:
    print(fileobject)  # TextIOWrapper
    "write data to the file"
    fileobject.write("My name is Noha\n")
    fileobject.write("I works at ITI\n")
    fileobject.writelines(["I works at ITI\n", "I lives in Cairo"])
    fileobject.close()  # save data to the file