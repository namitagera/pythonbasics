# Get details of loan

money_owe = float(input("How much do you owe?"))
apr = float(input("What is the apr?"))
payment = float(input("How much will you pay of each month?"))
months = int(input("How many months?"))

monthy_rate = apr/100/12

for i in range(months):

    # Calculate interest to pay 
    interest_paid = money_owe * monthy_rate

    # Add in interest 
    money_owe = money_owe + interest_paid

    if (money_owe - payment) < 0:
        print("The last payment is ", money_owe)
        print("You paid the loan off in", i+1, "months.")
        break

    # Make payment
    money_owe = money_owe - payment
    
    print("Paid" , payment, " of which", interest_paid , "was interest", end = " ")

print("Now I owe", money_owe)