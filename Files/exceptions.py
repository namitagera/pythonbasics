def remainer_division(a,b):
    if b == 0 or a == 0:
        raise Exception("Divisor cannot be 0") 
    result = a // b
    remainder = a % b
    print(a,"/", b, "is", result, "remainder", remainder)

# main program 

remainer_division(0,10)
