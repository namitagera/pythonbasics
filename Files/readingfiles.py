
#with open("acroyms.txt") as file:
#    result = file.read()
#    print(result)

#    result = file.readline()
#    print(result)

#    result = file.readlines()
#    for line in result:
#        print(line)

#    for line in file:
#        print(line)

## or can close file like 
#file = open("acronyms.txt")
#try:
#    #do file operations here
#    pass
#finally:
#    file.close()

## final code

look_up = input("What acronym would you like?")
found = False
with open("acronyms.txt") as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
if not found:
    print("Does not exist")

