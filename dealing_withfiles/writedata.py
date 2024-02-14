"""
    open ---> open file
    mode ==> "w"  ---> if file doesn't exist --> python will try
     to create

     when you open file with w --> mode --> open file for writing
     starting from the beginning of the file === remove old content
"""

try:
    fileobject= open("mycv.txt", "w")
except Exception as e:
    print(e)
else:
    print(fileobject)  # TextIOWrapper
    "write data to the file"
    fileobject.write("My name is Noha\n")
    fileobject.write("I works at ITI\n")
    fileobject.writelines(["I works at ITI\n", "I lives in Cairo"])
    # fileobject.close()  # save data to the file