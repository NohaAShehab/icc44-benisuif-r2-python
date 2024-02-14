"""
    open ---> open file
    mode ==> "r"  ---> if file doesn't exist --> raise exception
"""

try:
    fileobject= open("names.txt", "r")
except Exception as e:
    print(e)
else:
    print(fileobject)  # TextIOWrapper
    """ read file content into one string """
    data = fileobject.read()  # string
    print(data)
    """ move file object to the beginning of file"""
    fileobject.seek(0)
    """ read file line by line """
    lines = fileobject.readlines()  #list
    print(lines)
    """ check this """
    # lines = []
    # for line in fileobject:
    #     lines.append(line)
    # print(lines)
    #close fille
    fileobject.close()